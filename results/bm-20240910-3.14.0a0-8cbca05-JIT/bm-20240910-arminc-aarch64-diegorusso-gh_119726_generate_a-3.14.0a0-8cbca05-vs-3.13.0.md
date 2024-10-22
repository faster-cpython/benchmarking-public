# Results vs. 3.13.0

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: linux-aarch64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 376 ms: 1.23x slower                                                        |
| docutils       | 2.91 sec                                                 | 3.94 sec: 1.36x slower                                                      |
| html5lib       | 64.3 ms                                                  | 71.4 ms: 1.11x slower                                                       |
| tornado_http   | 131 ms                                                   | 151 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                    | 1.21x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 467 ms                                                   | 423 ms: 1.10x faster                                                        |
| async_tree_none            | 493 ms                                                   | 449 ms: 1.10x faster                                                        |
| async_tree_memoization     | 626 ms                                                   | 583 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                        |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                                        |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                       |
| async_generators           | 496 ms                                                   | 510 ms: 1.03x slower                                                        |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                      |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.28 sec: 1.04x slower                                                      |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                      |
| asyncio_tcp                | 568 ms                                                   | 632 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 87.8 ms: 1.07x faster                                                       |
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                       |
| regex_effbot   | 4.87 ms                                                  | 4.99 ms: 1.02x slower                                                       |
| regex_dna      | 246 ms                                                   | 255 ms: 1.03x slower                                                        |
| regex_compile  | 128 ms                                                   | 186 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                    | 1.11x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.34 us: 1.05x faster                                                       |
| unpickle             | 20.2 us                                                  | 19.3 us: 1.05x faster                                                       |
| pickle_list          | 5.34 us                                                  | 5.23 us: 1.02x faster                                                       |
| xml_etree_parse      | 188 ms                                                   | 187 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 147 ms                                                   | 149 ms: 1.02x slower                                                        |
| pickle               | 13.5 us                                                  | 13.7 us: 1.02x slower                                                       |
| unpickle_pure_python | 254 us                                                   | 264 us: 1.04x slower                                                        |
| json_dumps           | 13.4 ms                                                  | 13.9 ms: 1.04x slower                                                       |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                      |
| pickle_pure_python   | 359 us                                                   | 384 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, json_loads, xml_etree_process, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                       |
| django_template | 42.3 ms                                                  | 50.5 ms: 1.19x slower                                                       |
| genshi_text     | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                                       |
| genshi_xml      | 60.2 ms                                                  | 81.5 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.7 us: 1.35x faster                                                       |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                        |
| deepcopy                   | 451 us                                                   | 400 us: 1.13x faster                                                        |
| async_tree_none_tg         | 467 ms                                                   | 423 ms: 1.10x faster                                                        |
| async_tree_none            | 493 ms                                                   | 449 ms: 1.10x faster                                                        |
| float                      | 94.4 ms                                                  | 87.8 ms: 1.07x faster                                                       |
| async_tree_memoization     | 626 ms                                                   | 583 ms: 1.07x faster                                                        |
| scimark_sor                | 159 ms                                                   | 149 ms: 1.06x faster                                                        |
| deepcopy_reduce            | 4.07 us                                                  | 3.86 us: 1.05x faster                                                       |
| unpickle_list              | 6.65 us                                                  | 6.34 us: 1.05x faster                                                       |
| unpickle                   | 20.2 us                                                  | 19.3 us: 1.05x faster                                                       |
| pathlib                    | 22.4 ms                                                  | 21.7 ms: 1.03x faster                                                       |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                        |
| mako                       | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                       |
| regex_v8                   | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                       |
| pickle_list                | 5.34 us                                                  | 5.23 us: 1.02x faster                                                       |
| sqlite_synth               | 3.84 us                                                  | 3.79 us: 1.02x faster                                                       |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                        |
| xml_etree_parse            | 188 ms                                                   | 187 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 5.90 sec                                                 | 5.94 sec: 1.01x slower                                                      |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                                        |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                       |
| scimark_fft                | 447 ms                                                   | 454 ms: 1.02x slower                                                        |
| coverage                   | 98.5 ms                                                  | 100 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.02x slower                                                        |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.02x slower                                                       |
| logging_format             | 7.83 us                                                  | 8.00 us: 1.02x slower                                                       |
| thrift                     | 946 us                                                   | 966 us: 1.02x slower                                                        |
| regex_effbot               | 4.87 ms                                                  | 4.99 ms: 1.02x slower                                                       |
| async_generators           | 496 ms                                                   | 510 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.80 ms: 1.03x slower                                                       |
| spectral_norm              | 141 ms                                                   | 146 ms: 1.03x slower                                                        |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 254 us                                                   | 264 us: 1.04x slower                                                        |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                      |
| json_dumps                 | 13.4 ms                                                  | 13.9 ms: 1.04x slower                                                       |
| tomli_loads                | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                      |
| mdp                        | 3.36 sec                                                 | 3.50 sec: 1.04x slower                                                      |
| bench_mp_pool              | 7.30 ms                                                  | 7.61 ms: 1.04x slower                                                       |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.28 sec: 1.04x slower                                                      |
| logging_simple             | 7.04 us                                                  | 7.40 us: 1.05x slower                                                       |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.05x slower                                                       |
| bench_thread_pool          | 1.28 ms                                                  | 1.35 ms: 1.06x slower                                                       |
| pickle_pure_python         | 359 us                                                   | 384 us: 1.07x slower                                                        |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 192 us                                                   | 206 us: 1.07x slower                                                        |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                      |
| meteor_contest             | 113 ms                                                   | 124 ms: 1.09x slower                                                        |
| crypto_pyaes               | 82.7 ms                                                  | 90.5 ms: 1.09x slower                                                       |
| fannkuch                   | 452 ms                                                   | 497 ms: 1.10x slower                                                        |
| create_gc_cycles           | 2.12 ms                                                  | 2.34 ms: 1.11x slower                                                       |
| scimark_monte_carlo        | 83.8 ms                                                  | 92.8 ms: 1.11x slower                                                       |
| html5lib                   | 64.3 ms                                                  | 71.4 ms: 1.11x slower                                                       |
| asyncio_tcp                | 568 ms                                                   | 632 ms: 1.11x slower                                                        |
| deltablue                  | 3.85 ms                                                  | 4.33 ms: 1.12x slower                                                       |
| gc_traversal               | 4.53 ms                                                  | 5.13 ms: 1.13x slower                                                       |
| go                         | 163 ms                                                   | 184 ms: 1.13x slower                                                        |
| tornado_http               | 131 ms                                                   | 151 ms: 1.15x slower                                                        |
| pyflate                    | 556 ms                                                   | 641 ms: 1.15x slower                                                        |
| sqlglot_normalize          | 128 ms                                                   | 149 ms: 1.16x slower                                                        |
| raytrace                   | 298 ms                                                   | 348 ms: 1.17x slower                                                        |
| pycparser                  | 1.26 sec                                                 | 1.50 sec: 1.19x slower                                                      |
| django_template            | 42.3 ms                                                  | 50.5 ms: 1.19x slower                                                       |
| comprehensions             | 20.4 us                                                  | 24.6 us: 1.20x slower                                                       |
| 2to3                       | 306 ms                                                   | 376 ms: 1.23x slower                                                        |
| nqueens                    | 98.7 ms                                                  | 123 ms: 1.24x slower                                                        |
| richards_super             | 60.3 ms                                                  | 75.5 ms: 1.25x slower                                                       |
| richards                   | 53.5 ms                                                  | 67.3 ms: 1.26x slower                                                       |
| genshi_text                | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                                       |
| sqlglot_optimize           | 62.4 ms                                                  | 78.7 ms: 1.26x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                  | 1.74 ms: 1.26x slower                                                       |
| sqlglot_transpile          | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                                       |
| sympy_expand               | 455 ms                                                   | 601 ms: 1.32x slower                                                        |
| pprint_safe_repr           | 926 ms                                                   | 1.23 sec: 1.33x slower                                                      |
| chaos                      | 68.8 ms                                                  | 92.4 ms: 1.34x slower                                                       |
| sympy_integrate            | 21.0 ms                                                  | 28.2 ms: 1.35x slower                                                       |
| sympy_str                  | 264 ms                                                   | 355 ms: 1.35x slower                                                        |
| genshi_xml                 | 60.2 ms                                                  | 81.5 ms: 1.35x slower                                                       |
| pprint_pformat             | 1.90 sec                                                 | 2.57 sec: 1.35x slower                                                      |
| docutils                   | 2.91 sec                                                 | 3.94 sec: 1.36x slower                                                      |
| pylint                     | 343 ms                                                   | 475 ms: 1.38x slower                                                        |
| hexiom                     | 7.13 ms                                                  | 9.91 ms: 1.39x slower                                                       |
| regex_compile              | 128 ms                                                   | 186 ms: 1.45x slower                                                        |
| sympy_sum                  | 143 ms                                                   | 208 ms: 1.45x slower                                                        |
| generators                 | 37.8 ms                                                  | 58.1 ms: 1.54x slower                                                       |
| unpack_sequence            | 57.2 ns                                                  | 149 ns: 2.60x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                                |

Benchmark hidden because not significant (9): xml_etree_generate, json_loads, xml_etree_process, async_tree_cpu_io_mixed, pickle_dict, python_startup_no_site, json, pidigits, logging_silent
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x