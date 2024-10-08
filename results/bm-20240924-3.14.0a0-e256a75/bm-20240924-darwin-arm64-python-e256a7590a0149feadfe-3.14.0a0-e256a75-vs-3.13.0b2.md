# Results vs. 3.13.0b2

- fork: python
- ref: e256a7590a0149feadfe
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.01x faster
- HPT reliability: 71.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 160 ms: 1.01x faster                                                  |
| docutils       | 1.44 sec                                                   | 1.42 sec: 1.01x faster                                                |
| html5lib       | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 80.3 ms: 1.20x slower                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 674 ms: 1.14x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 706 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 579 ms: 1.03x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 60.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                 |
| regex_effbot   | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                 |
| regex_dna      | 149 ms                                                     | 144 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 66.8 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle              | 7.48 us                                                    | 7.39 us: 1.01x faster                                                 |
| unpickle            | 9.12 us                                                    | 9.05 us: 1.01x faster                                                 |
| xml_etree_generate  | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                 |
| pickle_dict         | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| json_loads          | 16.8 us                                                    | 16.8 us: 1.00x faster                                                 |
| json_dumps          | 6.23 ms                                                    | 6.26 ms: 1.00x slower                                                 |
| tomli_loads         | 1.47 sec                                                   | 1.47 sec: 1.01x slower                                                |
| pickle_list         | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| xml_etree_process   | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| pickle_pure_python  | 179 us                                                     | 183 us: 1.02x slower                                                  |
| xml_etree_parse     | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| xml_etree_iterparse | 71.5 ms                                                    | 73.5 ms: 1.03x slower                                                 |
| unpickle_list       | 2.88 us                                                    | 2.98 us: 1.03x slower                                                 |
| Geometric mean      | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.7 ms: 1.04x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| mako            | 6.99 ms                                                    | 7.21 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 143 us: 1.43x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.5 us: 1.36x faster                                                 |
| go                               | 101 ms                                                     | 79.2 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.22x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 674 ms: 1.14x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.7 ms: 1.11x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 706 ms: 1.09x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                                  |
| html5lib                         | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                     | 144 ms: 1.03x faster                                                  |
| scimark_lu                       | 66.9 ms                                                    | 64.8 ms: 1.03x faster                                                 |
| thrift                           | 435 us                                                     | 424 us: 1.03x faster                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.70 ms: 1.03x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 66.8 ms: 1.03x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 92.6 ms: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 455 ms: 1.02x faster                                                  |
| coverage                         | 45.0 ms                                                    | 44.1 ms: 1.02x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 929 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.39 us: 1.01x faster                                                 |
| async_generators                 | 281 ms                                                     | 278 ms: 1.01x faster                                                  |
| genshi_text                      | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                                 |
| scimark_fft                      | 181 ms                                                     | 179 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                                   | 1.42 sec: 1.01x faster                                                |
| deltablue                        | 2.14 ms                                                    | 2.12 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| create_gc_cycles                 | 897 us                                                     | 889 us: 1.01x faster                                                  |
| unpickle                         | 9.12 us                                                    | 9.05 us: 1.01x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                 |
| 2to3                             | 161 ms                                                     | 160 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| pyflate                          | 321 ms                                                     | 319 ms: 1.01x faster                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| json_loads                       | 16.8 us                                                    | 16.8 us: 1.00x faster                                                 |
| spectral_norm                    | 66.4 ms                                                    | 66.2 ms: 1.00x faster                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.4 ms: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| logging_silent                   | 60.1 ns                                                    | 60.3 ns: 1.00x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.26 ms: 1.00x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.47 sec: 1.01x slower                                                |
| telco                            | 4.60 ms                                                    | 4.63 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| nbody                            | 59.6 ms                                                    | 60.2 ms: 1.01x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.0 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 900 us: 1.01x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 740 us: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.8 ms: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 53.0 ms: 1.01x slower                                                 |
| raytrace                         | 147 ms                                                     | 149 ms: 1.02x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 454 us: 1.02x slower                                                  |
| richards                         | 31.8 ms                                                    | 32.4 ms: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.1 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.12 sec: 1.02x slower                                                |
| pickle_pure_python               | 179 us                                                     | 183 us: 1.02x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.5 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 579 ms: 1.03x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 36.2 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.21 ms: 1.03x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.98 us: 1.03x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 15.7 ms: 1.04x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 12.8 ms: 1.04x slower                                                 |
| fannkuch                         | 248 ms                                                     | 259 ms: 1.04x slower                                                  |
| chaos                            | 34.0 ms                                                    | 35.6 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 92.6 us: 1.06x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.07x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 80.3 ms: 1.20x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (20): async_tree_io_tg, dulwich_log, float, async_tree_eager_memoization, json, logging_format, asyncio_websockets, pathlib, sympy_str, sympy_sum, gc_traversal, sqlglot_optimize, unpickle_pure_python, hexiom, sqlglot_normalize, async_tree_eager_cpu_io_mixed, pycparser, async_tree_cpu_io_mixed_tg, asyncio_tcp, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 71.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.50x