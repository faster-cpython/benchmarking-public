# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_likely
- machine: windows-amd64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 250 ms: 1.02x slower                                                       |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                      |
| tornado_http   | 108 ms                                                      | 99.5 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 554 ms: 2.00x faster                                                       |
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                      |
| nbody          | 71.3 ms                                                     | 55.0 ms: 1.30x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_compile  | 106 ms                                                      | 92.9 ms: 1.14x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 143 us: 1.28x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.99 us: 1.01x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.0 us: 1.05x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.52 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.7 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.13 ms: 1.76x faster                                                      |
| django_template | 28.9 ms                                                     | 27.7 ms: 1.04x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.85x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 554 ms: 2.00x faster                                                       |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.13 ms: 1.76x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.1 ns: 1.69x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                       |
| scimark_sor              | 106 ms                                                      | 65.1 ms: 1.63x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.2 ms: 1.55x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.1 ms: 1.54x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                      |
| go                       | 139 ms                                                      | 92.0 ms: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 53.9 ms: 1.43x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                      |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| generators               | 32.4 ms                                                     | 23.9 ms: 1.35x faster                                                      |
| richards_super           | 52.2 ms                                                     | 38.6 ms: 1.35x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 908 us: 1.34x faster                                                       |
| float                    | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                      |
| deepcopy                 | 255 us                                                      | 194 us: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                      |
| nbody                    | 71.3 ms                                                     | 55.0 ms: 1.30x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                     |
| raytrace                 | 273 ms                                                      | 213 ms: 1.28x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 143 us: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 740 ms: 1.26x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 972 ms: 1.25x faster                                                       |
| pylint                   | 350 ms                                                      | 282 ms: 1.24x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.3 ms: 1.24x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 480 ms: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.21 ms: 1.22x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.21x faster                                                      |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                      |
| thrift                   | 617 us                                                      | 527 us: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.16x faster                                                     |
| regex_compile            | 106 ms                                                      | 92.9 ms: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 845 us: 1.13x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 650 ms: 1.13x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.25 ms: 1.09x faster                                                      |
| tornado_http             | 108 ms                                                      | 99.5 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| fannkuch                 | 256 ms                                                      | 240 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.7 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                      |
| sympy_sum                | 107 ms                                                      | 104 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.99 us: 1.01x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                      |
| 2to3                     | 246 ms                                                      | 250 ms: 1.02x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| sqlglot_normalize        | 205 ms                                                      | 212 ms: 1.03x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.9 ms: 1.04x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.0 us: 1.05x slower                                                      |
| sympy_expand             | 314 ms                                                      | 332 ms: 1.06x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.7 ms: 1.07x slower                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 43.4 ms: 1.09x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.52 us: 1.10x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.7 ms: 1.21x slower                                                      |
| async_generators         | 222 ms                                                      | 268 ms: 1.21x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.2 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 89.7 ms: 1.45x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 59.5 ns: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.41 ms: 1.76x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (5): genshi_text, meteor_contest, docutils, logging_simple, sympy_str
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown