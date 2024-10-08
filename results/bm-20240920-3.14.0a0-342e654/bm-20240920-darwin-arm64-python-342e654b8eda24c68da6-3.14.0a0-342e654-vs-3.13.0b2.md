# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.01x faster
- HPT reliability: 63.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| html5lib       | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 82.2 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.14x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 185 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 536 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.05x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 122 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 579 ms: 1.03x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 255 ms: 1.07x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.4 ms: 1.00x faster                                                 |
| nbody          | 59.6 ms                                                    | 60.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                                 |
| regex_effbot   | 2.58 ms                                                    | 2.53 ms: 1.02x faster                                                 |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.39 us: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 141 us: 1.00x slower                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.47 sec: 1.00x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                                 |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                  |
| unpickle_list        | 2.88 us                                                    | 2.94 us: 1.02x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.0 ms: 1.12x faster                                                 |
| python_startup         | 15.2 ms                                                    | 13.9 ms: 1.09x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.0 ms: 1.00x slower                                                 |
| mako            | 6.99 ms                                                    | 7.06 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 20.1 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.7 us: 1.35x faster                                                 |
| go                               | 101 ms                                                     | 79.1 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.22x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.14x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 11.0 ms: 1.12x faster                                                 |
| generators                       | 22.9 ms                                                    | 20.7 ms: 1.11x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.09x faster                                                  |
| python_startup                   | 15.2 ms                                                    | 13.9 ms: 1.09x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.08x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 185 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 536 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.05x faster                                                  |
| html5lib                         | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| thrift                           | 435 us                                                     | 420 us: 1.04x faster                                                  |
| scimark_lu                       | 66.9 ms                                                    | 64.8 ms: 1.03x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.70 ms: 1.03x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 122 ms: 1.03x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.53 ms: 1.02x faster                                                 |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 93.1 ms: 1.02x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.1 ms: 1.02x faster                                                 |
| pprint_pformat                   | 947 ms                                                     | 932 ms: 1.02x faster                                                  |
| coverage                         | 45.0 ms                                                    | 44.3 ms: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 458 ms: 1.01x faster                                                  |
| genshi_text                      | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.39 us: 1.01x faster                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| async_generators                 | 281 ms                                                     | 278 ms: 1.01x faster                                                  |
| scimark_fft                      | 181 ms                                                     | 179 ms: 1.01x faster                                                  |
| json                             | 2.93 ms                                                    | 2.91 ms: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.02 us: 1.01x faster                                                 |
| sympy_sum                        | 69.2 ms                                                    | 68.8 ms: 1.01x faster                                                 |
| spectral_norm                    | 66.4 ms                                                    | 66.0 ms: 1.01x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.01x faster                                                 |
| float                            | 48.6 ms                                                    | 48.4 ms: 1.00x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.00x faster                                                 |
| hexiom                           | 4.06 ms                                                    | 4.05 ms: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.45 ms: 1.00x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.32 us: 1.00x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 226 ms: 1.00x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 30.0 ms: 1.00x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 141 us: 1.00x slower                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.47 sec: 1.00x slower                                                |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 901 us: 1.00x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| richards                         | 31.8 ms                                                    | 32.0 ms: 1.01x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 737 us: 1.01x slower                                                  |
| nbody                            | 59.6 ms                                                    | 60.1 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| mako                             | 6.99 ms                                                    | 7.06 ms: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 900 us: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                                 |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 452 us: 1.01x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 60.9 ns: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.2 ms: 1.01x slower                                                 |
| raytrace                         | 147 ms                                                     | 149 ms: 1.02x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.1 ms: 1.02x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 35.9 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.2 ms: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.94 us: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.12 sec: 1.02x slower                                                |
| async_tree_io                    | 563 ms                                                     | 579 ms: 1.03x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.74 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 20.1 ms: 1.04x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.6 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 92.2 us: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 262 ms: 1.06x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 255 ms: 1.07x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.07x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 82.2 ms: 1.23x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (16): async_tree_eager_memoization, asyncio_tcp_ssl, docutils, pyflate, async_tree_eager_cpu_io_mixed, xml_etree_generate, json_loads, unpickle, sympy_str, deltablue, pidigits, 2to3, scimark_monte_carlo, asyncio_tcp, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 63.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.39x