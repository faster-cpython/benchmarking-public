# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-amd64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 234 ms: 1.05x faster                                                      |
| chameleon      | 5.79 ms                                                     | 4.73 ms: 1.22x faster                                                     |
| docutils       | 1.92 sec                                                    | 2.45 sec: 1.27x slower                                                    |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                     |
| tornado_http   | 108 ms                                                      | 86.4 ms: 1.25x faster                                                     |
| Geometric mean | (ref)                                                       | 1.10x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 638 ms                                                      | 2.23 sec: 3.50x slower                                                    |
| async_tree_none         | 435 ms                                                      | 1.78 sec: 4.10x slower                                                    |
| async_tree_memoization  | 526 ms                                                      | 2.29 sec: 4.35x slower                                                    |
| async_tree_io           | 1.11 sec                                                    | 7.14 sec: 6.44x slower                                                    |
| Geometric mean          | (ref)                                                       | 4.48x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 54.9 ms: 1.30x faster                                                     |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                      |
| float          | 61.7 ms                                                     | 80.3 ms: 1.30x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.6 ms: 1.27x faster                                                     |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                     |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.56 ms: 1.65x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 180 us: 1.50x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.46x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                    |
| unpickle             | 9.09 us                                                     | 8.38 us: 1.08x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                     |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                     |
| pickle               | 6.85 us                                                     | 7.13 us: 1.04x slower                                                     |
| pickle_list          | 2.75 us                                                     | 2.90 us: 1.05x slower                                                     |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                                     |
| xml_etree_generate   | 55.5 ms                                                     | 59.9 ms: 1.08x slower                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 124 ms: 1.28x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 93.1 ms: 1.43x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.13x slower                                                     |
| python_startup_no_site | 15.5 ms                                                     | 20.9 ms: 1.34x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.23 ms: 1.73x faster                                                     |
| django_template | 28.9 ms                                                     | 22.5 ms: 1.29x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 71.9 us: 4.67x faster                                                     |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                     |
| mako                     | 9.03 ms                                                     | 5.23 ms: 1.73x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 55.7 ns: 1.70x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 45.5 ms: 1.70x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 5.56 ms: 1.65x faster                                                     |
| richards_super           | 52.2 ms                                                     | 32.5 ms: 1.61x faster                                                     |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.60x faster                                                     |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.57x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                     |
| pyflate                  | 409 ms                                                      | 266 ms: 1.54x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.0 ms: 1.51x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 180 us: 1.50x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 42.0 ms: 1.49x faster                                                     |
| raytrace                 | 273 ms                                                      | 184 ms: 1.48x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.1 ms: 1.46x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.46x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 846 us: 1.44x faster                                                      |
| go                       | 139 ms                                                      | 99.1 ms: 1.40x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                    |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.28 ms: 1.34x faster                                                     |
| nbody                    | 71.3 ms                                                     | 54.9 ms: 1.30x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 944 ms: 1.29x faster                                                      |
| django_template          | 28.9 ms                                                     | 22.5 ms: 1.29x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 462 ms: 1.28x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 22.5 us: 1.28x faster                                                     |
| scimark_sor              | 106 ms                                                      | 83.2 ms: 1.28x faster                                                     |
| regex_compile            | 106 ms                                                      | 83.6 ms: 1.27x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.67 sec: 1.27x faster                                                    |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.16 ms: 1.26x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                     |
| tornado_http             | 108 ms                                                      | 86.4 ms: 1.25x faster                                                     |
| fannkuch                 | 256 ms                                                      | 205 ms: 1.24x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 69.2 ms: 1.24x faster                                                     |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.23x faster                                                    |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                     |
| chameleon                | 5.79 ms                                                     | 4.73 ms: 1.22x faster                                                     |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.21x faster                                                     |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.20x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                     |
| sympy_str                | 194 ms                                                      | 167 ms: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.16x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 832 us: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                      |
| pycparser                | 930 ms                                                      | 829 ms: 1.12x faster                                                      |
| deepcopy                 | 255 us                                                      | 228 us: 1.12x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 184 ms: 1.12x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                                     |
| mypy2                    | 555 ms                                                      | 505 ms: 1.10x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                     |
| unpickle                 | 9.09 us                                                     | 8.38 us: 1.08x faster                                                     |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                     |
| aiohttp                  | 995 us                                                      | 932 us: 1.07x faster                                                      |
| create_gc_cycles         | 800 us                                                      | 750 us: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.34 us: 1.07x faster                                                     |
| logging_simple           | 6.22 us                                                     | 5.84 us: 1.07x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                     |
| 2to3                     | 246 ms                                                      | 234 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                     |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                                     |
| gc_traversal             | 1.41 ms                                                     | 1.37 ms: 1.03x faster                                                     |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                     |
| pathlib                  | 75.7 ms                                                     | 77.1 ms: 1.02x slower                                                     |
| pickle                   | 6.85 us                                                     | 7.13 us: 1.04x slower                                                     |
| pickle_list              | 2.75 us                                                     | 2.90 us: 1.05x slower                                                     |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 59.9 ms: 1.08x slower                                                     |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.13x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 71.3 ms: 1.15x slower                                                     |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.19x slower                                                     |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.21x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.45 sec: 1.27x slower                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 124 ms: 1.28x slower                                                      |
| float                    | 61.7 ms                                                     | 80.3 ms: 1.30x slower                                                     |
| async_generators         | 222 ms                                                      | 291 ms: 1.31x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.9 ms: 1.34x slower                                                     |
| xml_etree_iterparse      | 65.0 ms                                                     | 93.1 ms: 1.43x slower                                                     |
| pylint                   | 350 ms                                                      | 577 ms: 1.65x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 66.6 ns: 1.68x slower                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 2.23 sec: 3.50x slower                                                    |
| async_tree_none          | 435 ms                                                      | 1.78 sec: 4.10x slower                                                    |
| async_tree_memoization   | 526 ms                                                      | 2.29 sec: 4.35x slower                                                    |
| async_tree_io            | 1.11 sec                                                    | 7.14 sec: 6.44x slower                                                    |
| thrift                   | 617 us                                                      | 8.98 ms: 14.54x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: unknown