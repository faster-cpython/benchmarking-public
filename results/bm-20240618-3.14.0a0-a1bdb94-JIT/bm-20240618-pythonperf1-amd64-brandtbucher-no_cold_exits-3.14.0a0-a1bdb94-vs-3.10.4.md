# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                    |
| html5lib       | 51.0 ms                                                     | 36.4 ms: 1.40x faster                                                     |
| tornado_http   | 108 ms                                                      | 83.1 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                       | 1.22x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 223 ms: 1.95x faster                                                      |
| async_tree_memoization  | 526 ms                                                      | 272 ms: 1.94x faster                                                      |
| async_tree_io           | 1.11 sec                                                    | 598 ms: 1.85x faster                                                      |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                      |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                     |
| nbody          | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                       | 1.24x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.8 ms: 1.24x faster                                                     |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                     |
| regex_v8       | 15.4 ms                                                     | 18.9 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                       | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.69 ms: 1.61x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 168 us: 1.60x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.47x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                    |
| xml_etree_process    | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.6 ms: 1.09x faster                                                     |
| xml_etree_generate   | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 91.4 ms: 1.06x faster                                                     |
| unpickle             | 9.09 us                                                     | 8.78 us: 1.03x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                     |
| pickle_list          | 2.75 us                                                     | 2.82 us: 1.03x slower                                                     |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                     |
| pickle               | 6.85 us                                                     | 7.20 us: 1.05x slower                                                     |
| unpickle_list        | 2.71 us                                                     | 2.88 us: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                                     |
| python_startup_no_site | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.28 ms: 1.71x faster                                                     |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 42.4 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.11x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.10 ms: 2.00x faster                                                     |
| async_tree_none          | 435 ms                                                      | 223 ms: 1.95x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 272 ms: 1.94x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 15.4 us: 1.87x faster                                                     |
| async_tree_io            | 1.11 sec                                                    | 598 ms: 1.85x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 53.1 ns: 1.78x faster                                                     |
| mako                     | 9.03 ms                                                     | 5.28 ms: 1.71x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 45.7 ms: 1.69x faster                                                     |
| richards_super           | 52.2 ms                                                     | 31.8 ms: 1.64x faster                                                     |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 5.69 ms: 1.61x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                     |
| raytrace                 | 273 ms                                                      | 170 ms: 1.61x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 168 us: 1.60x faster                                                      |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 771 us: 1.58x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 466 ms: 1.57x faster                                                      |
| go                       | 139 ms                                                      | 88.6 ms: 1.57x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.2 ms: 1.54x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                     |
| pylint                   | 350 ms                                                      | 230 ms: 1.52x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.1 ms: 1.51x faster                                                     |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 998 us: 1.48x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.47x faster                                                    |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.47x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                    |
| html5lib                 | 51.0 ms                                                     | 36.4 ms: 1.40x faster                                                     |
| float                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                     |
| nbody                    | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 930 ms: 1.31x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 454 ms: 1.30x faster                                                      |
| tornado_http             | 108 ms                                                      | 83.1 ms: 1.30x faster                                                     |
| scimark_sor              | 106 ms                                                      | 81.7 ms: 1.30x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.72 us: 1.28x faster                                                     |
| thrift                   | 617 us                                                      | 491 us: 1.26x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.62 ms: 1.24x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.19 ms: 1.24x faster                                                     |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 773 us: 1.24x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 69.3 ms: 1.24x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.24x faster                                                    |
| regex_compile            | 106 ms                                                      | 85.8 ms: 1.24x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                     |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.8 ms: 1.18x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                     |
| logging_format           | 6.76 us                                                     | 5.92 us: 1.14x faster                                                     |
| logging_simple           | 6.22 us                                                     | 5.46 us: 1.14x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 35.0 ms: 1.14x faster                                                     |
| fannkuch                 | 256 ms                                                      | 225 ms: 1.14x faster                                                      |
| pycparser                | 930 ms                                                      | 825 ms: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 173 ms: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 60.0 ms: 1.11x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                    |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.6 ms: 1.09x faster                                                     |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                     |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 91.4 ms: 1.06x faster                                                     |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                     |
| unpickle                 | 9.09 us                                                     | 8.78 us: 1.03x faster                                                     |
| pathlib                  | 75.7 ms                                                     | 74.9 ms: 1.01x faster                                                     |
| python_startup           | 20.6 ms                                                     | 20.4 ms: 1.01x faster                                                     |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                     |
| pickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                     |
| genshi_xml               | 41.0 ms                                                     | 42.4 ms: 1.03x slower                                                     |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                     |
| pickle                   | 6.85 us                                                     | 7.20 us: 1.05x slower                                                     |
| unpickle_list            | 2.71 us                                                     | 2.88 us: 1.06x slower                                                     |
| python_startup_no_site   | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 68.6 ms: 1.10x slower                                                     |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                     |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 905 us: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.47 ms: 1.13x slower                                                     |
| coverage                 | 39.0 ms                                                     | 44.5 ms: 1.14x slower                                                     |
| regex_v8                 | 15.4 ms                                                     | 18.9 ms: 1.22x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                              |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown