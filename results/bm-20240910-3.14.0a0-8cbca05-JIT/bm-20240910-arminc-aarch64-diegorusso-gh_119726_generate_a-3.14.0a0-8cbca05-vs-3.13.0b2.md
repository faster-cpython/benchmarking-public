# Results vs. 3.13.0b2

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: linux-aarch64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 376 ms: 1.23x slower                                                        |
| docutils       | 3.10 sec                                                     | 3.94 sec: 1.27x slower                                                      |
| html5lib       | 66.1 ms                                                      | 71.4 ms: 1.08x slower                                                       |
| tornado_http   | 128 ms                                                       | 151 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 423 ms: 1.13x faster                                                        |
| async_tree_memoization     | 645 ms                                                       | 583 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                        |
| async_tree_none            | 492 ms                                                       | 449 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                      |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 761 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 87.8 ms: 1.04x faster                                                       |
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                                        |
| regex_compile  | 128 ms                                                       | 186 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 110 ms: 1.03x faster                                                        |
| unpickle_list        | 6.52 us                                                      | 6.34 us: 1.03x faster                                                       |
| json_loads           | 32.1 us                                                      | 31.3 us: 1.03x faster                                                       |
| unpickle             | 19.8 us                                                      | 19.3 us: 1.03x faster                                                       |
| xml_etree_process    | 80.8 ms                                                      | 79.7 ms: 1.01x faster                                                       |
| pickle_list          | 5.27 us                                                      | 5.23 us: 1.01x faster                                                       |
| pickle_dict          | 37.6 us                                                      | 38.0 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                                        |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                      |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                                       |
| unpickle_pure_python | 251 us                                                       | 264 us: 1.05x slower                                                        |
| json_dumps           | 13.1 ms                                                      | 13.9 ms: 1.06x slower                                                       |
| pickle_pure_python   | 359 us                                                       | 384 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                       |
| django_template | 42.3 ms                                                      | 50.5 ms: 1.19x slower                                                       |
| genshi_text     | 27.4 ms                                                      | 34.9 ms: 1.27x slower                                                       |
| genshi_xml      | 60.4 ms                                                      | 81.5 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.7 us: 1.35x faster                                                       |
| async_tree_none_tg         | 476 ms                                                       | 423 ms: 1.13x faster                                                        |
| deepcopy                   | 448 us                                                       | 400 us: 1.12x faster                                                        |
| async_tree_memoization     | 645 ms                                                       | 583 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                        |
| async_tree_none            | 492 ms                                                       | 449 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                      |
| scimark_sor                | 159 ms                                                       | 149 ms: 1.07x faster                                                        |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                        |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 4.04 us                                                      | 3.86 us: 1.05x faster                                                       |
| float                      | 91.4 ms                                                      | 87.8 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 761 ms: 1.04x faster                                                        |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                        |
| sqlite_synth               | 3.90 us                                                      | 3.79 us: 1.03x faster                                                       |
| xml_etree_generate         | 114 ms                                                       | 110 ms: 1.03x faster                                                        |
| unpickle_list              | 6.52 us                                                      | 6.34 us: 1.03x faster                                                       |
| json_loads                 | 32.1 us                                                      | 31.3 us: 1.03x faster                                                       |
| unpickle                   | 19.8 us                                                      | 19.3 us: 1.03x faster                                                       |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                                        |
| xml_etree_process          | 80.8 ms                                                      | 79.7 ms: 1.01x faster                                                       |
| mako                       | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                       |
| pickle_list                | 5.27 us                                                      | 5.23 us: 1.01x faster                                                       |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                       |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                        |
| pickle_dict                | 37.6 us                                                      | 38.0 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                        |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                        |
| bpe_tokeniser              | 5.83 sec                                                     | 5.94 sec: 1.02x slower                                                      |
| scimark_fft                | 445 ms                                                       | 454 ms: 1.02x slower                                                        |
| logging_format             | 7.82 us                                                      | 8.00 us: 1.02x slower                                                       |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                      |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                       |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.02x slower                                                       |
| logging_silent             | 133 ns                                                       | 137 ns: 1.03x slower                                                        |
| logging_simple             | 7.21 us                                                      | 7.40 us: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.28 sec: 1.03x slower                                                      |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.80 ms: 1.04x slower                                                       |
| async_generators           | 488 ms                                                       | 510 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 251 us                                                       | 264 us: 1.05x slower                                                        |
| mdp                        | 3.33 sec                                                     | 3.50 sec: 1.05x slower                                                      |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.06x slower                                                        |
| json_dumps                 | 13.1 ms                                                      | 13.9 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 193 us                                                       | 206 us: 1.06x slower                                                        |
| pickle_pure_python         | 359 us                                                       | 384 us: 1.07x slower                                                        |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.07x slower                                                       |
| html5lib                   | 66.1 ms                                                      | 71.4 ms: 1.08x slower                                                       |
| bench_mp_pool              | 7.03 ms                                                      | 7.61 ms: 1.08x slower                                                       |
| asyncio_tcp                | 584 ms                                                       | 632 ms: 1.08x slower                                                        |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.09x slower                                                        |
| fannkuch                   | 451 ms                                                       | 497 ms: 1.10x slower                                                        |
| crypto_pyaes               | 82.0 ms                                                      | 90.5 ms: 1.10x slower                                                       |
| deltablue                  | 3.88 ms                                                      | 4.33 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 82.3 ms                                                      | 92.8 ms: 1.13x slower                                                       |
| go                         | 161 ms                                                       | 184 ms: 1.15x slower                                                        |
| pyflate                    | 557 ms                                                       | 641 ms: 1.15x slower                                                        |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.15x slower                                                        |
| raytrace                   | 297 ms                                                       | 348 ms: 1.17x slower                                                        |
| tornado_http               | 128 ms                                                       | 151 ms: 1.18x slower                                                        |
| django_template            | 42.3 ms                                                      | 50.5 ms: 1.19x slower                                                       |
| comprehensions             | 20.5 us                                                      | 24.6 us: 1.20x slower                                                       |
| richards                   | 55.9 ms                                                      | 67.3 ms: 1.21x slower                                                       |
| richards_super             | 62.3 ms                                                      | 75.5 ms: 1.21x slower                                                       |
| sqlglot_parse              | 1.42 ms                                                      | 1.74 ms: 1.23x slower                                                       |
| pycparser                  | 1.22 sec                                                     | 1.50 sec: 1.23x slower                                                      |
| 2to3                       | 305 ms                                                       | 376 ms: 1.23x slower                                                        |
| nqueens                    | 98.9 ms                                                      | 123 ms: 1.24x slower                                                        |
| sqlglot_optimize           | 62.6 ms                                                      | 78.7 ms: 1.26x slower                                                       |
| docutils                   | 3.10 sec                                                     | 3.94 sec: 1.27x slower                                                      |
| genshi_text                | 27.4 ms                                                      | 34.9 ms: 1.27x slower                                                       |
| sqlglot_transpile          | 1.71 ms                                                      | 2.20 ms: 1.29x slower                                                       |
| sympy_expand               | 457 ms                                                       | 601 ms: 1.31x slower                                                        |
| pprint_safe_repr           | 933 ms                                                       | 1.23 sec: 1.32x slower                                                      |
| pprint_pformat             | 1.93 sec                                                     | 2.57 sec: 1.33x slower                                                      |
| sympy_str                  | 265 ms                                                       | 355 ms: 1.34x slower                                                        |
| genshi_xml                 | 60.4 ms                                                      | 81.5 ms: 1.35x slower                                                       |
| sympy_integrate            | 20.9 ms                                                      | 28.2 ms: 1.35x slower                                                       |
| chaos                      | 68.3 ms                                                      | 92.4 ms: 1.35x slower                                                       |
| dulwich_log                | 58.5 ms                                                      | 80.7 ms: 1.38x slower                                                       |
| hexiom                     | 7.08 ms                                                      | 9.91 ms: 1.40x slower                                                       |
| pylint                     | 337 ms                                                       | 475 ms: 1.41x slower                                                        |
| sympy_sum                  | 144 ms                                                       | 208 ms: 1.45x slower                                                        |
| regex_compile              | 128 ms                                                       | 186 ms: 1.45x slower                                                        |
| generators                 | 37.1 ms                                                      | 58.1 ms: 1.57x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (9): xml_etree_parse, coroutines, gc_traversal, regex_v8, json, pidigits, regex_effbot, thrift, create_gc_cycles
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x