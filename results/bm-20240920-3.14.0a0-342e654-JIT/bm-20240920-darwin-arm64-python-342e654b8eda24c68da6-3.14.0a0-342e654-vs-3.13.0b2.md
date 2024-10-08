# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.03x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.09x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                                |
| html5lib       | 31.2 ms                                                    | 33.8 ms: 1.09x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 84.5 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                      | 1.13x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 700 ms: 1.10x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 541 ms: 1.04x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 201 ms: 1.04x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 461 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 589 ms: 1.05x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.7 ms: 1.06x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.1 ms: 1.06x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 63.6 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_effbot   | 2.58 ms                                                    | 2.49 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 74.3 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 34.1 ms: 1.09x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.08x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 50.1 ms: 1.05x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.92 us: 1.01x faster                                                 |
| pickle               | 7.48 us                                                    | 7.42 us: 1.01x faster                                                 |
| json_dumps           | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 178 us: 1.00x faster                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.3 ms: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.23 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (3): pickle_dict, unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.5 ms: 1.07x faster                                                 |
| python_startup         | 15.2 ms                                                    | 14.4 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.45 ms: 1.08x faster                                                 |
| django_template | 19.4 ms                                                    | 22.6 ms: 1.16x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.6 ms: 1.19x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 41.1 ms: 1.37x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.1 us: 1.41x faster                                                 |
| deepcopy                         | 204 us                                                     | 153 us: 1.33x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 700 ms: 1.10x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 34.1 ms: 1.09x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.45 ms: 1.08x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 87.7 ms: 1.08x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.08x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 11.5 ms: 1.07x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| float                            | 48.6 ms                                                    | 46.1 ms: 1.06x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 63.4 ms: 1.05x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                                |
| xml_etree_generate               | 52.7 ms                                                    | 50.1 ms: 1.05x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 14.4 ms: 1.05x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 541 ms: 1.04x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 201 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.49 ms: 1.04x faster                                                 |
| thrift                           | 435 us                                                     | 425 us: 1.03x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 22.9 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| pickle_list                      | 2.96 us                                                    | 2.92 us: 1.01x faster                                                 |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                                  |
| json                             | 2.93 ms                                                    | 2.91 ms: 1.01x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.42 us: 1.01x faster                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.19 ms: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.02 us: 1.01x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.8 ms: 1.00x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 178 us: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.01x slower                                                |
| go                               | 101 ms                                                     | 101 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 904 us: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 67.0 ms: 1.01x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.3 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.23 us: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| pyflate                          | 321 ms                                                     | 326 ms: 1.02x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.58 us: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 461 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.02x slower                                                 |
| async_generators                 | 281 ms                                                     | 290 ms: 1.03x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.80 ms: 1.04x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 62.8 ns: 1.04x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 51.7 ms: 1.04x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 589 ms: 1.05x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 49.4 ms: 1.05x slower                                                 |
| dulwich_log                      | 27.6 ms                                                    | 29.0 ms: 1.05x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 469 us: 1.05x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.7 ms: 1.06x slower                                                 |
| fannkuch                         | 248 ms                                                     | 263 ms: 1.06x slower                                                  |
| nbody                            | 59.6 ms                                                    | 63.6 ms: 1.07x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 75.2 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 257 ms: 1.07x slower                                                  |
| pycparser                        | 632 ms                                                     | 678 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.98 ms: 1.07x slower                                                 |
| generators                       | 22.9 ms                                                    | 24.6 ms: 1.08x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 94.3 us: 1.08x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 74.3 ms: 1.08x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 33.8 ms: 1.09x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 75.2 ms: 1.09x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                                |
| sympy_str                        | 131 ms                                                     | 143 ms: 1.09x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 247 ms: 1.09x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 509 ms: 1.09x slower                                                  |
| 2to3                             | 161 ms                                                     | 176 ms: 1.09x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.35 ms: 1.10x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 1.04 sec: 1.10x slower                                                |
| sqlglot_normalize                | 166 ms                                                     | 183 ms: 1.10x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 11.5 ms: 1.11x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 58.2 ms: 1.12x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 47.4 ms: 1.12x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 35.5 ms: 1.15x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 850 us: 1.16x slower                                                  |
| django_template                  | 19.4 ms                                                    | 22.6 ms: 1.16x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.04 ms: 1.16x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.74 ms: 1.17x slower                                                 |
| raytrace                         | 147 ms                                                     | 173 ms: 1.17x slower                                                  |
| chaos                            | 34.0 ms                                                    | 40.1 ms: 1.18x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.6 ms: 1.19x slower                                                 |
| pylint                           | 170 ms                                                     | 205 ms: 1.20x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 12.8 us: 1.26x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 84.5 ms: 1.27x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 46.4 ms: 1.32x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 41.1 ms: 1.37x slower                                                 |
| richards                         | 31.8 ms                                                    | 44.4 ms: 1.39x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, pickle_dict, gc_traversal, logging_format, unpickle_list, json_loads, async_tree_eager_memoization, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.55x