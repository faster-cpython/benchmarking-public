# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_8192
- machine: linux-x86_64
- commit hash: 1236a9d
- commit date: 2024-11-12
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 324 ms: 1.39x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                |
| async_tree_io              | 1.16 sec                                               | 860 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 581 ms: 1.25x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.9 ms: 1.17x faster                                               |
| float          | 84.7 ms                                                | 76.6 ms: 1.11x faster                                               |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.01x faster                                               |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 78.9 ms: 1.13x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                               |
| json_loads           | 28.5 us                                                | 27.0 us: 1.05x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                               |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.17x faster                                               |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 324 ms: 1.39x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                               |
| async_tree_io              | 1.16 sec                                               | 860 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                |
| richards                   | 45.8 ms                                                | 36.7 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 581 ms: 1.25x faster                                                |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.25x faster                                               |
| richards_super             | 51.5 ms                                                | 41.8 ms: 1.23x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 68.0 ms: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.05 us: 1.20x faster                                               |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.17x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 64.0 ms: 1.17x faster                                               |
| nbody                      | 97.0 ms                                                | 82.9 ms: 1.17x faster                                               |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                               |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 78.9 ms: 1.13x faster                                               |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                               |
| float                      | 84.7 ms                                                | 76.6 ms: 1.11x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.08x faster                                               |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                                |
| fannkuch                   | 417 ms                                                 | 392 ms: 1.06x faster                                                |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                               |
| logging_silent             | 104 ns                                                 | 100.0 ns: 1.04x faster                                              |
| sympy_str                  | 300 ms                                                 | 289 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                               |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                               |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                |
| dulwich_log                | 68.5 ms                                                | 67.0 ms: 1.02x faster                                               |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                               |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.59 ms: 1.01x faster                                               |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.00x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.01x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                               |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 867 us: 1.03x slower                                                |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                              |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                               |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.57 ms: 1.07x slower                                               |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                               |
| hexiom                     | 6.41 ms                                                | 7.02 ms: 1.09x slower                                               |
| generators                 | 31.2 ms                                                | 36.3 ms: 1.16x slower                                               |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.26x slower                                               |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 78.2 ms: 3.26x slower                                               |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (3): sqlglot_optimize, spectral_norm, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241112-3.14.0a1+-1236a9d-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.072x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x