# Results vs. 3.10.4

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 5e813c5
- commit date: 2024-11-04
- overall geometric mean: 1.412x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                      |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 637 ms: 2.78x faster                                                      |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.72x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 339 ms: 2.56x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 101 ms: 1.52x faster                                                      |
| float          | 117 ms                                                 | 77.7 ms: 1.51x faster                                                     |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                     |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 330 us: 1.47x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                     |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.12x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                     |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                      |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 637 ms: 2.78x faster                                                      |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.72x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 339 ms: 2.56x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.35 ms: 2.36x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                      |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                      |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                      |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 32.0 us: 1.83x faster                                                     |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                      |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                      |
| richards_super           | 94.7 ms                                                | 54.6 ms: 1.74x faster                                                     |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                                     |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 69.9 ms: 1.69x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                     |
| richards                 | 79.3 ms                                                | 48.2 ms: 1.64x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.36 ms: 1.63x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                     |
| pyflate                  | 716 ms                                                 | 461 ms: 1.55x faster                                                      |
| nbody                    | 154 ms                                                 | 101 ms: 1.52x faster                                                      |
| float                    | 117 ms                                                 | 77.7 ms: 1.51x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.80 us: 1.49x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                    |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                      |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 330 us: 1.47x faster                                                      |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                     |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                      |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                    |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                     |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                      |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                      |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                     |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                                     |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                      |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.98 ms: 1.30x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                     |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                    |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                      |
| scimark_fft              | 466 ms                                                 | 387 ms: 1.20x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 840 us: 1.17x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                     |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                      |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.12x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                     |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                                     |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                      |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                     |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.47 ms: 1.23x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                              |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241104-3.14.0a1+-5e813c5/bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.412x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x