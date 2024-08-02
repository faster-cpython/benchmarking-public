# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 35.7 ms: 1.43x faster                                                      |
| tornado_http   | 108 ms                                                      | 82.9 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 225 ms: 1.94x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 272 ms: 1.93x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 599 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.0 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.4 ms: 1.29x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 18.5 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 167 us: 1.61x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.86 us: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.03x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.8 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.27 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 39.4 ms: 1.04x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.12x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.13 ms: 1.97x faster                                                      |
| async_tree_none          | 435 ms                                                      | 225 ms: 1.94x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 272 ms: 1.93x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.5 us: 1.85x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 599 ms: 1.85x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 46.7 ms: 1.65x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.2 ms: 1.61x faster                                                      |
| pyflate                  | 409 ms                                                      | 254 ms: 1.61x faster                                                       |
| raytrace                 | 273 ms                                                      | 170 ms: 1.61x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 167 us: 1.61x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| go                       | 139 ms                                                      | 87.4 ms: 1.59x faster                                                      |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 781 us: 1.56x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.4 ms: 1.55x faster                                                      |
| deepcopy                 | 255 us                                                      | 166 us: 1.54x faster                                                       |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 482 ms: 1.52x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.0 ms: 1.51x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 980 us: 1.51x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.8 ms: 1.50x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.46x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.7 ms: 1.43x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                                     |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.0 ms: 1.37x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.0 ms: 1.37x faster                                                      |
| tornado_http             | 108 ms                                                      | 82.9 ms: 1.31x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.70 us: 1.30x faster                                                      |
| regex_compile            | 106 ms                                                      | 82.4 ms: 1.29x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 462 ms: 1.28x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.39 sec: 1.28x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 751 us: 1.28x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 956 ms: 1.28x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.3 ms: 1.27x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 495 us: 1.25x faster                                                       |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.21 ms: 1.23x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 72.3 ms: 1.19x faster                                                      |
| pycparser                | 930 ms                                                      | 795 ms: 1.17x faster                                                       |
| fannkuch                 | 256 ms                                                      | 219 ms: 1.17x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.65 us: 1.16x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 57.6 ms: 1.16x faster                                                      |
| logging_format           | 6.76 us                                                     | 5.91 us: 1.14x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.48 us: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.4 ms: 1.12x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.8 ms: 1.04x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 39.4 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.86 us: 1.03x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 75.1 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.03x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.8 us: 1.04x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.27 us: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.6 ms: 1.14x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 915 us: 1.14x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                      |
| coverage                 | 39.0 ms                                                     | 45.6 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.18x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 18.5 ms: 1.20x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown