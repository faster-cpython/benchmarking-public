# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.2 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 266 ms: 1.98x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 577 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.89x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.7 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 88.1 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_compile  | 106 ms                                                      | 91.6 ms: 1.16x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.6 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.04 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.7 ms: 1.12x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.96x faster                                                       |
| async_tree_none          | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 266 ms: 1.98x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 577 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 88.6 ms: 1.57x faster                                                      |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.57x faster                                                      |
| pylint                   | 350 ms                                                      | 227 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.4 ns: 1.47x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| raytrace                 | 273 ms                                                      | 190 ms: 1.44x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.7 ms: 1.42x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 522 ms: 1.40x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.7 us: 1.39x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 892 us: 1.36x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.1 ms: 1.36x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.31x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.30x faster                                                     |
| mako                     | 9.03 ms                                                     | 7.04 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.56 ms: 1.26x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.8 ms: 1.25x faster                                                      |
| pyflate                  | 409 ms                                                      | 326 ms: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.0 ms: 1.19x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                                     |
| pycparser                | 930 ms                                                      | 791 ms: 1.18x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.2 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.6 ms: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.7 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.9 ms: 1.12x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.7 ms: 1.12x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.7 ms: 1.11x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| float                    | 61.7 ms                                                     | 56.7 ms: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 563 ms: 1.05x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 73.9 ms: 1.05x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 64.1 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.69 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.37 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.6 ms: 1.04x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.8 ms: 1.04x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.5 ms: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                       |
| scimark_fft              | 187 ms                                                      | 211 ms: 1.13x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.3 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.16x slower                                                      |
| fannkuch                 | 256 ms                                                      | 307 ms: 1.20x slower                                                       |
| nbody                    | 71.3 ms                                                     | 88.1 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.16 ms: 1.31x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (2): json, logging_format
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown