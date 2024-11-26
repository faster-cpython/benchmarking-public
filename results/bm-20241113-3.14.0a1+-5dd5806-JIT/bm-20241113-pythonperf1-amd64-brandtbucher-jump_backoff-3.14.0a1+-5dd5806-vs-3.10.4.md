# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-amd64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.220x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.84 sec: 1.04x faster                                                    |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                     |
| Geometric mean | (ref)                                                       | 1.14x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 544 ms: 2.04x faster                                                      |
| async_tree_none         | 435 ms                                                      | 214 ms: 2.03x faster                                                      |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                      |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                      |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                     |
| nbody          | 71.3 ms                                                     | 56.7 ms: 1.26x faster                                                     |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.6 ms: 1.21x faster                                                     |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.09x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 109 us: 1.68x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                     |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                    |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                     |
| xml_etree_generate   | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.3 ms: 1.04x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                     |
| python_startup         | 20.6 ms                                                     | 24.0 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.12 ms: 1.76x faster                                                     |
| django_template | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 44.0 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 544 ms: 2.04x faster                                                      |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.03x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                     |
| mako                     | 9.03 ms                                                     | 5.12 ms: 1.76x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.72x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 109 us: 1.68x faster                                                      |
| scimark_sor              | 106 ms                                                      | 63.5 ms: 1.67x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.9 ns: 1.64x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 53.3 ms: 1.61x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.7 ms: 1.56x faster                                                     |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                     |
| go                       | 139 ms                                                      | 93.1 ms: 1.49x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                     |
| generators               | 32.4 ms                                                     | 22.3 ms: 1.45x faster                                                     |
| pylint                   | 350 ms                                                      | 244 ms: 1.43x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 55.7 ms: 1.39x faster                                                     |
| richards_super           | 52.2 ms                                                     | 37.7 ms: 1.38x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 878 us: 1.38x faster                                                      |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                     |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                                      |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                    |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                     |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 944 ms: 1.29x faster                                                      |
| raytrace                 | 273 ms                                                      | 214 ms: 1.28x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 467 ms: 1.27x faster                                                      |
| nbody                    | 71.3 ms                                                     | 56.7 ms: 1.26x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                     |
| richards                 | 42.4 ms                                                     | 33.9 ms: 1.25x faster                                                     |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.21 ms: 1.23x faster                                                     |
| regex_compile            | 106 ms                                                      | 87.6 ms: 1.21x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                     |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 5.05 ms: 1.14x faster                                                     |
| sympy_sum                | 107 ms                                                      | 94.9 ms: 1.13x faster                                                     |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                      |
| thrift                   | 617 us                                                      | 552 us: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.63 sec: 1.10x faster                                                    |
| django_template          | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                     |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                      |
| sympy_str                | 194 ms                                                      | 184 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                     |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                     |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.84 sec: 1.04x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 64.1 ms: 1.04x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 93.3 ms: 1.04x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 38.7 ms: 1.03x faster                                                     |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                     |
| pathlib                  | 75.7 ms                                                     | 75.0 ms: 1.01x faster                                                     |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 205 ms                                                      | 208 ms: 1.01x slower                                                      |
| sympy_expand             | 314 ms                                                      | 320 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.04x slower                                                     |
| genshi_xml               | 41.0 ms                                                     | 44.0 ms: 1.07x slower                                                     |
| telco                    | 3.94 ms                                                     | 4.25 ms: 1.08x slower                                                     |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                     |
| python_startup           | 20.6 ms                                                     | 24.0 ms: 1.16x slower                                                     |
| async_generators         | 222 ms                                                      | 268 ms: 1.21x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                     |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 86.6 ms: 1.40x slower                                                     |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                              |

Benchmark hidden because not significant (2): logging_simple, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-pythonperf1-amd64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.220x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown