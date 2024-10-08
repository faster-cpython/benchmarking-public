# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.09x slower                                       |
| chameleon      | 4.27 ms                                                    | 4.75 ms: 1.11x slower                                      |
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                     |
| html5lib       | 31.2 ms                                                    | 36.1 ms: 1.16x slower                                      |
| tornado_http   | 66.7 ms                                                    | 86.2 ms: 1.29x slower                                      |
| Geometric mean | (ref)                                                      | 1.13x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 654 ms: 1.17x faster                                       |
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.14x faster                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 372 ms: 1.04x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 346 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 523 ms: 1.12x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 68.4 ms: 1.13x slower                                      |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 143 ms: 1.14x slower                                       |
| async_tree_eager_memoization     | 152 ms                                                     | 174 ms: 1.14x slower                                       |
| async_tree_eager_tg              | 41.4 ms                                                    | 49.5 ms: 1.20x slower                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 542 ms: 1.20x slower                                       |
| async_tree_none                  | 209 ms                                                     | 256 ms: 1.22x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 695 ms: 1.23x slower                                       |
| async_tree_io                    | 563 ms                                                     | 710 ms: 1.26x slower                                       |
| async_tree_memoization           | 260 ms                                                     | 333 ms: 1.28x slower                                       |
| async_tree_none_tg               | 198 ms                                                     | 270 ms: 1.37x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 336 ms: 1.40x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.15x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| float          | 48.6 ms                                                    | 56.5 ms: 1.16x slower                                      |
| nbody          | 59.6 ms                                                    | 71.5 ms: 1.20x slower                                      |
| Geometric mean | (ref)                                                      | 1.12x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x faster                                      |
| regex_effbot   | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                      |
| regex_dna      | 149 ms                                                     | 158 ms: 1.06x slower                                       |
| regex_compile  | 68.5 ms                                                    | 74.6 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.34 us: 1.02x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.0 us: 1.01x faster                                      |
| unpickle             | 9.12 us                                                    | 9.04 us: 1.01x faster                                      |
| pickle_list          | 2.96 us                                                    | 2.94 us: 1.00x faster                                      |
| json_loads           | 16.8 us                                                    | 16.8 us: 1.00x faster                                      |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.04x slower                                       |
| unpickle_list        | 2.88 us                                                    | 2.99 us: 1.04x slower                                      |
| tomli_loads          | 1.47 sec                                                   | 1.53 sec: 1.05x slower                                     |
| json_dumps           | 6.23 ms                                                    | 6.54 ms: 1.05x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 39.3 ms: 1.06x slower                                      |
| xml_etree_generate   | 52.7 ms                                                    | 56.0 ms: 1.06x slower                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 76.3 ms: 1.07x slower                                      |
| unpickle_pure_python | 141 us                                                     | 155 us: 1.10x slower                                       |
| pickle_pure_python   | 179 us                                                     | 200 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.6 ms: 1.09x slower                                      |
| python_startup_no_site | 12.3 ms                                                    | 14.7 ms: 1.20x slower                                      |
| Geometric mean         | (ref)                                                      | 1.14x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.35 ms: 1.05x slower                                      |
| genshi_xml      | 29.9 ms                                                    | 33.0 ms: 1.10x slower                                      |
| django_template | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                      |
| genshi_text     | 13.9 ms                                                    | 15.7 ms: 1.13x slower                                      |
| Geometric mean  | (ref)                                                      | 1.10x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles                 | 897 us                                                     | 705 us: 1.27x faster                                       |
| typing_runtime_protocols         | 87.6 us                                                    | 73.2 us: 1.20x faster                                      |
| async_tree_eager_io_tg           | 768 ms                                                     | 654 ms: 1.17x faster                                       |
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.14x faster                                       |
| crypto_pyaes                     | 49.5 ms                                                    | 47.9 ms: 1.03x faster                                      |
| telco                            | 4.60 ms                                                    | 4.47 ms: 1.03x faster                                      |
| pickle                           | 7.48 us                                                    | 7.34 us: 1.02x faster                                      |
| gc_traversal                     | 2.45 ms                                                    | 2.41 ms: 1.02x faster                                      |
| pickle_dict                      | 18.3 us                                                    | 18.0 us: 1.01x faster                                      |
| unpickle                         | 9.12 us                                                    | 9.04 us: 1.01x faster                                      |
| pickle_list                      | 2.96 us                                                    | 2.94 us: 1.00x faster                                      |
| json_loads                       | 16.8 us                                                    | 16.8 us: 1.00x faster                                      |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                       |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x faster                                      |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| docutils                         | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                     |
| json                             | 2.93 ms                                                    | 2.97 ms: 1.01x slower                                      |
| mdp                              | 1.53 sec                                                   | 1.56 sec: 1.02x slower                                     |
| regex_effbot                     | 2.58 ms                                                    | 2.63 ms: 1.02x slower                                      |
| sympy_integrate                  | 10.3 ms                                                    | 10.5 ms: 1.02x slower                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 48.1 ms: 1.02x slower                                      |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.32 sec: 1.02x slower                                     |
| sympy_expand                     | 226 ms                                                     | 232 ms: 1.03x slower                                       |
| sqlite_synth                     | 1.55 us                                                    | 1.60 us: 1.03x slower                                      |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.04x slower                                       |
| meteor_contest                   | 70.3 ms                                                    | 72.9 ms: 1.04x slower                                      |
| unpickle_list                    | 2.88 us                                                    | 2.99 us: 1.04x slower                                      |
| sympy_str                        | 131 ms                                                     | 136 ms: 1.04x slower                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 372 ms: 1.04x slower                                       |
| sympy_sum                        | 69.2 ms                                                    | 72.0 ms: 1.04x slower                                      |
| go                               | 101 ms                                                     | 105 ms: 1.04x slower                                       |
| pyflate                          | 321 ms                                                     | 335 ms: 1.04x slower                                       |
| tomli_loads                      | 1.47 sec                                                   | 1.53 sec: 1.05x slower                                     |
| coverage                         | 45.0 ms                                                    | 47.1 ms: 1.05x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 346 ms: 1.05x slower                                       |
| json_dumps                       | 6.23 ms                                                    | 6.54 ms: 1.05x slower                                      |
| thrift                           | 435 us                                                     | 457 us: 1.05x slower                                       |
| mako                             | 6.99 ms                                                    | 7.35 ms: 1.05x slower                                      |
| deepcopy_reduce                  | 1.82 us                                                    | 1.92 us: 1.06x slower                                      |
| regex_dna                        | 149 ms                                                     | 158 ms: 1.06x slower                                       |
| dulwich_log                      | 27.6 ms                                                    | 29.2 ms: 1.06x slower                                      |
| pprint_pformat                   | 947 ms                                                     | 1.00 sec: 1.06x slower                                     |
| xml_etree_process                | 37.1 ms                                                    | 39.3 ms: 1.06x slower                                      |
| async_generators                 | 281 ms                                                     | 299 ms: 1.06x slower                                       |
| xml_etree_generate               | 52.7 ms                                                    | 56.0 ms: 1.06x slower                                      |
| pprint_safe_repr                 | 465 ms                                                     | 495 ms: 1.06x slower                                       |
| xml_etree_iterparse              | 71.5 ms                                                    | 76.3 ms: 1.07x slower                                      |
| asyncio_tcp                      | 402 ms                                                     | 430 ms: 1.07x slower                                       |
| sqlglot_optimize                 | 30.9 ms                                                    | 33.3 ms: 1.08x slower                                      |
| richards                         | 31.8 ms                                                    | 34.3 ms: 1.08x slower                                      |
| deepcopy                         | 204 us                                                     | 221 us: 1.08x slower                                       |
| sqlglot_normalize                | 166 ms                                                     | 180 ms: 1.08x slower                                       |
| richards_super                   | 35.2 ms                                                    | 38.2 ms: 1.08x slower                                      |
| scimark_lu                       | 66.9 ms                                                    | 72.8 ms: 1.09x slower                                      |
| regex_compile                    | 68.5 ms                                                    | 74.6 ms: 1.09x slower                                      |
| fannkuch                         | 248 ms                                                     | 271 ms: 1.09x slower                                       |
| bench_thread_pool                | 447 us                                                     | 488 us: 1.09x slower                                       |
| python_startup                   | 15.2 ms                                                    | 16.6 ms: 1.09x slower                                      |
| 2to3                             | 161 ms                                                     | 176 ms: 1.09x slower                                       |
| scimark_sor                      | 94.9 ms                                                    | 104 ms: 1.09x slower                                       |
| pycparser                        | 632 ms                                                     | 692 ms: 1.09x slower                                       |
| scimark_monte_carlo              | 42.5 ms                                                    | 46.6 ms: 1.10x slower                                      |
| sqlglot_parse                    | 732 us                                                     | 805 us: 1.10x slower                                       |
| sqlglot_transpile                | 891 us                                                     | 980 us: 1.10x slower                                       |
| genshi_xml                       | 29.9 ms                                                    | 33.0 ms: 1.10x slower                                      |
| unpickle_pure_python             | 141 us                                                     | 155 us: 1.10x slower                                       |
| django_template                  | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                      |
| nqueens                          | 52.2 ms                                                    | 58.1 ms: 1.11x slower                                      |
| scimark_fft                      | 181 ms                                                     | 201 ms: 1.11x slower                                       |
| chameleon                        | 4.27 ms                                                    | 4.75 ms: 1.11x slower                                      |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.40 sec: 1.11x slower                                     |
| comprehensions                   | 10.2 us                                                    | 11.3 us: 1.11x slower                                      |
| spectral_norm                    | 66.4 ms                                                    | 74.0 ms: 1.12x slower                                      |
| pathlib                          | 23.3 ms                                                    | 26.0 ms: 1.12x slower                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.10 ms: 1.12x slower                                      |
| deepcopy_memo                    | 22.6 us                                                    | 25.3 us: 1.12x slower                                      |
| pickle_pure_python               | 179 us                                                     | 200 us: 1.12x slower                                       |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 523 ms: 1.12x slower                                       |
| genshi_text                      | 13.9 ms                                                    | 15.7 ms: 1.13x slower                                      |
| async_tree_eager                 | 60.3 ms                                                    | 68.4 ms: 1.13x slower                                      |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 143 ms: 1.14x slower                                       |
| flaskblogging                    | 3.61 ms                                                    | 4.11 ms: 1.14x slower                                      |
| async_tree_eager_memoization     | 152 ms                                                     | 174 ms: 1.14x slower                                       |
| deltablue                        | 2.14 ms                                                    | 2.44 ms: 1.14x slower                                      |
| coroutines                       | 15.8 ms                                                    | 18.2 ms: 1.15x slower                                      |
| logging_format                   | 3.31 us                                                    | 3.82 us: 1.15x slower                                      |
| html5lib                         | 31.2 ms                                                    | 36.1 ms: 1.16x slower                                      |
| logging_simple                   | 3.04 us                                                    | 3.53 us: 1.16x slower                                      |
| float                            | 48.6 ms                                                    | 56.5 ms: 1.16x slower                                      |
| logging_silent                   | 60.1 ns                                                    | 70.6 ns: 1.17x slower                                      |
| hexiom                           | 4.06 ms                                                    | 4.77 ms: 1.17x slower                                      |
| async_tree_eager_tg              | 41.4 ms                                                    | 49.5 ms: 1.20x slower                                      |
| python_startup_no_site           | 12.3 ms                                                    | 14.7 ms: 1.20x slower                                      |
| nbody                            | 59.6 ms                                                    | 71.5 ms: 1.20x slower                                      |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 542 ms: 1.20x slower                                       |
| chaos                            | 34.0 ms                                                    | 41.2 ms: 1.21x slower                                      |
| raytrace                         | 147 ms                                                     | 179 ms: 1.22x slower                                       |
| generators                       | 22.9 ms                                                    | 28.0 ms: 1.22x slower                                      |
| async_tree_none                  | 209 ms                                                     | 256 ms: 1.22x slower                                       |
| async_tree_io_tg                 | 565 ms                                                     | 695 ms: 1.23x slower                                       |
| async_tree_io                    | 563 ms                                                     | 710 ms: 1.26x slower                                       |
| async_tree_memoization           | 260 ms                                                     | 333 ms: 1.28x slower                                       |
| aiohttp                          | 997 us                                                     | 1.28 ms: 1.29x slower                                      |
| tornado_http                     | 66.7 ms                                                    | 86.2 ms: 1.29x slower                                      |
| gunicorn                         | 1.04 ms                                                    | 1.38 ms: 1.33x slower                                      |
| async_tree_none_tg               | 198 ms                                                     | 270 ms: 1.37x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 336 ms: 1.40x slower                                       |
| mypy2                            | 379 ms                                                     | 611 ms: 1.61x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.09x slower                                               |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dask
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.49x