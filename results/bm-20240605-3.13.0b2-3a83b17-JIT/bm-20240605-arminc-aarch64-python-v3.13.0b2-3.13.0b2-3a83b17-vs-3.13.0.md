# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 360 ms: 1.18x slower                                         |
| chameleon      | 9.02 ms                                                  | 9.18 ms: 1.02x slower                                        |
| docutils       | 2.91 sec                                                 | 3.52 sec: 1.21x slower                                       |
| html5lib       | 64.3 ms                                                  | 71.7 ms: 1.11x slower                                        |
| tornado_http   | 131 ms                                                   | 139 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                    | 1.11x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 620 ms: 1.05x faster                                         |
| asyncio_websockets         | 656 ms                                                   | 659 ms: 1.01x slower                                         |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                        |
| async_generators           | 496 ms                                                   | 508 ms: 1.02x slower                                         |
| async_tree_none            | 493 ms                                                   | 508 ms: 1.03x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                       |
| async_tree_none_tg         | 467 ms                                                   | 485 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 818 ms: 1.07x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 671 ms: 1.07x slower                                         |
| asyncio_tcp                | 568 ms                                                   | 618 ms: 1.09x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 806 ms: 1.10x slower                                         |
| async_tree_io_tg           | 1.09 sec                                                 | 1.23 sec: 1.13x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.25 sec: 1.13x slower                                       |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 88.7 ms: 1.06x faster                                        |
| nbody          | 114 ms                                                   | 116 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                        |
| regex_compile  | 128 ms                                                   | 175 ms: 1.36x slower                                         |
| Geometric mean | (ref)                                                    | 1.07x slower                                                 |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.7 us: 1.02x faster                                        |
| pickle_list          | 5.34 us                                                  | 5.30 us: 1.01x faster                                        |
| xml_etree_iterparse  | 147 ms                                                   | 148 ms: 1.01x slower                                         |
| json_loads           | 31.4 us                                                  | 32.1 us: 1.02x slower                                        |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                       |
| unpickle_pure_python | 254 us                                                   | 278 us: 1.09x slower                                         |
| pickle_pure_python   | 359 us                                                   | 398 us: 1.11x slower                                         |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (7): pickle_dict, unpickle_list, json_dumps, xml_etree_process, xml_etree_parse, pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 15.3 ms: 1.15x slower                                        |
| python_startup_no_site | 8.75 ms                                                  | 10.9 ms: 1.24x slower                                        |
| Geometric mean         | (ref)                                                    | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.0 ms: 1.03x faster                                        |
| django_template | 42.3 ms                                                  | 49.6 ms: 1.17x slower                                        |
| genshi_text     | 27.7 ms                                                  | 35.4 ms: 1.28x slower                                        |
| genshi_xml      | 60.2 ms                                                  | 83.4 ms: 1.39x slower                                        |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 929 ms: 1.27x faster                                         |
| float                      | 94.4 ms                                                  | 88.7 ms: 1.06x faster                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 620 ms: 1.05x faster                                         |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                        |
| mako                       | 13.3 ms                                                  | 13.0 ms: 1.03x faster                                        |
| deepcopy_memo              | 51.0 us                                                  | 49.7 us: 1.03x faster                                        |
| unpickle                   | 20.2 us                                                  | 19.7 us: 1.02x faster                                        |
| sqlite_synth               | 3.84 us                                                  | 3.78 us: 1.02x faster                                        |
| pickle_list                | 5.34 us                                                  | 5.30 us: 1.01x faster                                        |
| asyncio_websockets         | 656 ms                                                   | 659 ms: 1.01x slower                                         |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                         |
| bpe_tokeniser              | 5.90 sec                                                 | 5.97 sec: 1.01x slower                                       |
| nbody                      | 114 ms                                                   | 116 ms: 1.01x slower                                         |
| chameleon                  | 9.02 ms                                                  | 9.18 ms: 1.02x slower                                        |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                        |
| thrift                     | 946 us                                                   | 965 us: 1.02x slower                                         |
| mdp                        | 3.36 sec                                                 | 3.44 sec: 1.02x slower                                       |
| json_loads                 | 31.4 us                                                  | 32.1 us: 1.02x slower                                        |
| json                       | 5.61 ms                                                  | 5.74 ms: 1.02x slower                                        |
| async_generators           | 496 ms                                                   | 508 ms: 1.02x slower                                         |
| fannkuch                   | 452 ms                                                   | 463 ms: 1.03x slower                                         |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                         |
| logging_format             | 7.83 us                                                  | 8.05 us: 1.03x slower                                        |
| async_tree_none            | 493 ms                                                   | 508 ms: 1.03x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                       |
| bench_thread_pool          | 1.28 ms                                                  | 1.32 ms: 1.03x slower                                        |
| pathlib                    | 22.4 ms                                                  | 23.2 ms: 1.03x slower                                        |
| meteor_contest             | 113 ms                                                   | 118 ms: 1.04x slower                                         |
| logging_simple             | 7.04 us                                                  | 7.31 us: 1.04x slower                                        |
| async_tree_none_tg         | 467 ms                                                   | 485 ms: 1.04x slower                                         |
| logging_silent             | 135 ns                                                   | 141 ns: 1.04x slower                                         |
| telco                      | 9.73 ms                                                  | 10.1 ms: 1.04x slower                                        |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                       |
| generators                 | 37.8 ms                                                  | 39.6 ms: 1.05x slower                                        |
| richards                   | 53.5 ms                                                  | 56.2 ms: 1.05x slower                                        |
| richards_super             | 60.3 ms                                                  | 63.4 ms: 1.05x slower                                        |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.94 ms: 1.05x slower                                        |
| spectral_norm              | 141 ms                                                   | 149 ms: 1.06x slower                                         |
| tornado_http               | 131 ms                                                   | 139 ms: 1.06x slower                                         |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.0 ms: 1.06x slower                                        |
| pycparser                  | 1.26 sec                                                 | 1.35 sec: 1.07x slower                                       |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 818 ms: 1.07x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 671 ms: 1.07x slower                                         |
| pyflate                    | 556 ms                                                   | 596 ms: 1.07x slower                                         |
| aiohttp                    | 1.19 ms                                                  | 1.28 ms: 1.07x slower                                        |
| typing_runtime_protocols   | 192 us                                                   | 207 us: 1.08x slower                                         |
| crypto_pyaes               | 82.7 ms                                                  | 89.1 ms: 1.08x slower                                        |
| raytrace                   | 298 ms                                                   | 321 ms: 1.08x slower                                         |
| asyncio_tcp                | 568 ms                                                   | 618 ms: 1.09x slower                                         |
| unpickle_pure_python       | 254 us                                                   | 278 us: 1.09x slower                                         |
| scimark_sor                | 159 ms                                                   | 174 ms: 1.09x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 806 ms: 1.10x slower                                         |
| go                         | 163 ms                                                   | 180 ms: 1.10x slower                                         |
| pickle_pure_python         | 359 us                                                   | 398 us: 1.11x slower                                         |
| deepcopy                   | 451 us                                                   | 502 us: 1.11x slower                                         |
| html5lib                   | 64.3 ms                                                  | 71.7 ms: 1.11x slower                                        |
| sqlglot_optimize           | 62.4 ms                                                  | 69.8 ms: 1.12x slower                                        |
| create_gc_cycles           | 2.12 ms                                                  | 2.38 ms: 1.12x slower                                        |
| flaskblogging              | 4.60 ms                                                  | 5.16 ms: 1.12x slower                                        |
| gc_traversal               | 4.53 ms                                                  | 5.08 ms: 1.12x slower                                        |
| dask                       | 350 ms                                                   | 393 ms: 1.12x slower                                         |
| sqlglot_normalize          | 128 ms                                                   | 144 ms: 1.13x slower                                         |
| async_tree_io_tg           | 1.09 sec                                                 | 1.23 sec: 1.13x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.25 sec: 1.13x slower                                       |
| bench_mp_pool              | 7.30 ms                                                  | 8.24 ms: 1.13x slower                                        |
| gunicorn                   | 1.20 ms                                                  | 1.36 ms: 1.13x slower                                        |
| comprehensions             | 20.4 us                                                  | 23.2 us: 1.14x slower                                        |
| sqlglot_parse              | 1.38 ms                                                  | 1.58 ms: 1.14x slower                                        |
| deepcopy_reduce            | 4.07 us                                                  | 4.68 us: 1.15x slower                                        |
| python_startup             | 13.3 ms                                                  | 15.3 ms: 1.15x slower                                        |
| sqlglot_transpile          | 1.73 ms                                                  | 2.00 ms: 1.16x slower                                        |
| django_template            | 42.3 ms                                                  | 49.6 ms: 1.17x slower                                        |
| 2to3                       | 306 ms                                                   | 360 ms: 1.18x slower                                         |
| sympy_expand               | 455 ms                                                   | 538 ms: 1.18x slower                                         |
| nqueens                    | 98.7 ms                                                  | 117 ms: 1.19x slower                                         |
| deltablue                  | 3.85 ms                                                  | 4.58 ms: 1.19x slower                                        |
| pprint_safe_repr           | 926 ms                                                   | 1.11 sec: 1.20x slower                                       |
| pylint                     | 343 ms                                                   | 414 ms: 1.21x slower                                         |
| docutils                   | 2.91 sec                                                 | 3.52 sec: 1.21x slower                                       |
| sympy_integrate            | 21.0 ms                                                  | 25.5 ms: 1.22x slower                                        |
| sympy_str                  | 264 ms                                                   | 321 ms: 1.22x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 2.31 sec: 1.22x slower                                       |
| python_startup_no_site     | 8.75 ms                                                  | 10.9 ms: 1.24x slower                                        |
| hexiom                     | 7.13 ms                                                  | 8.89 ms: 1.25x slower                                        |
| chaos                      | 68.8 ms                                                  | 87.1 ms: 1.27x slower                                        |
| sympy_sum                  | 143 ms                                                   | 183 ms: 1.27x slower                                         |
| genshi_text                | 27.7 ms                                                  | 35.4 ms: 1.28x slower                                        |
| scimark_lu                 | 139 ms                                                   | 183 ms: 1.31x slower                                         |
| regex_compile              | 128 ms                                                   | 175 ms: 1.36x slower                                         |
| genshi_xml                 | 60.2 ms                                                  | 83.4 ms: 1.39x slower                                        |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                 |

Benchmark hidden because not significant (11): pickle_dict, unpickle_list, coverage, json_dumps, regex_effbot, pidigits, xml_etree_process, regex_dna, xml_etree_parse, pickle, xml_etree_generate
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.09x