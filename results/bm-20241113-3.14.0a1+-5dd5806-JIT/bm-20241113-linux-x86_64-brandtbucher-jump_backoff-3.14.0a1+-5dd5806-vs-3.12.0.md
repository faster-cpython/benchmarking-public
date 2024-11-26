# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                 |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.38x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 987 ms: 1.20x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.8 ms: 1.16x faster                                                |
| float          | 84.7 ms                                                | 76.2 ms: 1.11x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                 |
| regex_dna      | 212 ms                                                 | 224 ms: 1.05x slower                                                 |
| regex_effbot   | 3.61 ms                                                | 3.83 ms: 1.06x slower                                                |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                               |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 82.8 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.16x faster                                                |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.38x faster                                                 |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                |
| comprehensions             | 21.8 us                                                | 17.7 us: 1.23x faster                                                |
| richards_super             | 51.5 ms                                                | 41.9 ms: 1.23x faster                                                |
| richards                   | 45.8 ms                                                | 37.5 ms: 1.22x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 987 ms: 1.20x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                               |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.19x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 69.2 ms: 1.18x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.16x faster                                                |
| nbody                      | 97.0 ms                                                | 83.8 ms: 1.16x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.12x faster                                                 |
| float                      | 84.7 ms                                                | 76.2 ms: 1.11x faster                                                |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.9 ms: 1.10x faster                                                |
| raytrace                   | 312 ms                                                 | 285 ms: 1.09x faster                                                 |
| logging_silent             | 104 ns                                                 | 95.5 ns: 1.09x faster                                                |
| json                       | 5.26 ms                                                | 4.83 ms: 1.09x faster                                                |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 82.8 ms: 1.08x faster                                                |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                                |
| pyflate                    | 482 ms                                                 | 453 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                                |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 161 ms: 1.05x faster                                                 |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                 |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                                |
| dulwich_log                | 68.5 ms                                                | 67.2 ms: 1.02x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 21.0 ms: 1.02x faster                                                |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                 |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                 |
| coroutines                 | 23.2 ms                                                | 23.1 ms: 1.00x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 55.7 ms: 1.02x slower                                                |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                               |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                                |
| telco                      | 7.10 ms                                                | 7.48 ms: 1.05x slower                                                |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.79 sec: 1.06x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.83 ms: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.15 ms: 1.12x slower                                                |
| generators                 | 31.2 ms                                                | 35.6 ms: 1.14x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.34 ms: 1.14x slower                                                |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (3): pickle_pure_python, spectral_norm, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.066x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x