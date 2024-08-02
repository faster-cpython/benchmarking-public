# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_align
- machine: windows-amd64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                                     |
| chameleon      | 5.79 ms                                                     | 5.08 ms: 1.14x faster                                                    |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                   |
| html5lib       | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                    |
| tornado_http   | 108 ms                                                      | 85.4 ms: 1.27x faster                                                    |
| Geometric mean | (ref)                                                       | 1.18x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 233 ms: 1.87x faster                                                     |
| async_tree_memoization  | 526 ms                                                      | 283 ms: 1.86x faster                                                     |
| async_tree_io           | 1.11 sec                                                    | 611 ms: 1.81x faster                                                     |
| async_tree_cpu_io_mixed | 638 ms                                                      | 404 ms: 1.58x faster                                                     |
| Geometric mean          | (ref)                                                       | 1.78x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.1 ms: 1.40x faster                                                    |
| float          | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                       | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.4 ms: 1.21x faster                                                    |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                    |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                       | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.65 ms: 1.62x faster                                                    |
| pickle_pure_python   | 270 us                                                      | 173 us: 1.56x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.44x faster                                                     |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                                   |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                    |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                    |
| xml_etree_generate   | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                    |
| xml_etree_parse      | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                    |
| unpickle             | 9.09 us                                                     | 8.68 us: 1.05x faster                                                    |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                    |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                    |
| pickle_list          | 2.75 us                                                     | 2.84 us: 1.03x slower                                                    |
| pickle_dict          | 17.2 us                                                     | 17.8 us: 1.04x slower                                                    |
| pickle               | 6.85 us                                                     | 7.55 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                    |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.00 ms: 1.81x faster                                                    |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                    |
| genshi_text     | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                    |
| genshi_xml      | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.99x faster                                                     |
| async_tree_none          | 435 ms                                                      | 233 ms: 1.87x faster                                                     |
| async_tree_memoization   | 526 ms                                                      | 283 ms: 1.86x faster                                                     |
| async_tree_io            | 1.11 sec                                                    | 611 ms: 1.81x faster                                                     |
| mako                     | 9.03 ms                                                     | 5.00 ms: 1.81x faster                                                    |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                    |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.71x faster                                                    |
| json_dumps               | 9.16 ms                                                     | 5.65 ms: 1.62x faster                                                    |
| spectral_norm            | 77.3 ms                                                     | 47.8 ms: 1.62x faster                                                    |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                    |
| pyflate                  | 409 ms                                                      | 259 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 404 ms: 1.58x faster                                                     |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.57x faster                                                    |
| pickle_pure_python       | 270 us                                                      | 173 us: 1.56x faster                                                     |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                     |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                    |
| asyncio_tcp              | 732 ms                                                      | 478 ms: 1.53x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 41.0 ms: 1.53x faster                                                    |
| generators               | 32.4 ms                                                     | 21.3 ms: 1.52x faster                                                    |
| sqlglot_parse            | 1.22 ms                                                     | 803 us: 1.51x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.9 ms: 1.51x faster                                                    |
| pylint                   | 350 ms                                                      | 237 ms: 1.48x faster                                                     |
| go                       | 139 ms                                                      | 94.5 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.45x faster                                                   |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.44x faster                                                     |
| richards                 | 42.4 ms                                                     | 29.5 ms: 1.44x faster                                                    |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                    |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                                    |
| nbody                    | 71.3 ms                                                     | 51.1 ms: 1.40x faster                                                    |
| float                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                    |
| html5lib                 | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                    |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 920 ms: 1.33x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 453 ms: 1.31x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                    |
| scimark_sor              | 106 ms                                                      | 83.4 ms: 1.27x faster                                                    |
| tornado_http             | 108 ms                                                      | 85.4 ms: 1.27x faster                                                    |
| scimark_lu               | 85.8 ms                                                     | 67.8 ms: 1.27x faster                                                    |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.66 ms: 1.23x faster                                                    |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                    |
| thrift                   | 617 us                                                      | 506 us: 1.22x faster                                                     |
| regex_compile            | 106 ms                                                      | 87.4 ms: 1.21x faster                                                    |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                                   |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                    |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                    |
| pycparser                | 930 ms                                                      | 803 ms: 1.16x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 833 us: 1.15x faster                                                     |
| sympy_sum                | 107 ms                                                      | 93.3 ms: 1.15x faster                                                    |
| chameleon                | 5.79 ms                                                     | 5.08 ms: 1.14x faster                                                    |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                    |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                     |
| fannkuch                 | 256 ms                                                      | 230 ms: 1.11x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 60.1 ms: 1.11x faster                                                    |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                    |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                    |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                     |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                    |
| sqlglot_optimize         | 39.8 ms                                                     | 36.7 ms: 1.09x faster                                                    |
| logging_format           | 6.76 us                                                     | 6.23 us: 1.09x faster                                                    |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                   |
| xml_etree_generate       | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                    |
| logging_simple           | 6.22 us                                                     | 5.79 us: 1.08x faster                                                    |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.05x faster                                                    |
| deepcopy                 | 255 us                                                      | 242 us: 1.05x faster                                                     |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                    |
| unpickle                 | 9.09 us                                                     | 8.68 us: 1.05x faster                                                    |
| genshi_text              | 19.8 ms                                                     | 18.9 ms: 1.05x faster                                                    |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                    |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                    |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                                     |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                    |
| pickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                    |
| pickle_dict              | 17.2 us                                                     | 17.8 us: 1.04x slower                                                    |
| pathlib                  | 75.7 ms                                                     | 78.7 ms: 1.04x slower                                                    |
| python_startup           | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                    |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                    |
| pickle                   | 6.85 us                                                     | 7.55 us: 1.10x slower                                                    |
| genshi_xml               | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                    |
| bench_mp_pool            | 62.0 ms                                                     | 70.1 ms: 1.13x slower                                                    |
| create_gc_cycles         | 800 us                                                      | 904 us: 1.13x slower                                                     |
| async_generators         | 222 ms                                                      | 254 ms: 1.15x slower                                                     |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                    |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                    |
| coverage                 | 39.0 ms                                                     | 46.0 ms: 1.18x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                             |

Benchmark hidden because not significant (2): flaskblogging, pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown