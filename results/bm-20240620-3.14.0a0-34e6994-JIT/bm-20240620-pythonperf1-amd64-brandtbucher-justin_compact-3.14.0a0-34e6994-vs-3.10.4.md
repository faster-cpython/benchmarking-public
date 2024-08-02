# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: windows-amd64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                     |
| html5lib       | 51.0 ms                                                     | 36.3 ms: 1.41x faster                                                      |
| tornado_http   | 108 ms                                                      | 83.3 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 272 ms: 1.93x faster                                                       |
| async_tree_none         | 435 ms                                                      | 227 ms: 1.92x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 604 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.82x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.6 ms: 1.41x faster                                                      |
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.2 ms: 1.29x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.3 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 168 us: 1.60x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 123 us: 1.49x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.41x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.7 ms: 1.09x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.70 us: 1.04x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.86 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.49 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.24 ms: 1.73x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.07 ms: 2.02x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 272 ms: 1.93x faster                                                       |
| async_tree_none          | 435 ms                                                      | 227 ms: 1.92x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.6 us: 1.85x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 604 ms: 1.83x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.7 ns: 1.73x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.24 ms: 1.73x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.1 ms: 1.71x faster                                                      |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.1 us: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| raytrace                 | 273 ms                                                      | 169 ms: 1.62x faster                                                       |
| pyflate                  | 409 ms                                                      | 253 ms: 1.62x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.70 ms: 1.61x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 168 us: 1.60x faster                                                       |
| go                       | 139 ms                                                      | 86.7 ms: 1.60x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 781 us: 1.56x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.9 ms: 1.54x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 476 ms: 1.54x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.4 ms: 1.53x faster                                                      |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 123 us: 1.49x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 991 us: 1.49x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.45x faster                                                     |
| richards                 | 42.4 ms                                                     | 30.0 ms: 1.41x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.41x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 36.3 ms: 1.41x faster                                                      |
| nbody                    | 71.3 ms                                                     | 50.6 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.39x faster                                                      |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 932 ms: 1.31x faster                                                       |
| tornado_http             | 108 ms                                                      | 83.3 ms: 1.30x faster                                                      |
| regex_compile            | 106 ms                                                      | 82.2 ms: 1.29x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 460 ms: 1.29x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.72 us: 1.28x faster                                                      |
| scimark_sor              | 106 ms                                                      | 83.0 ms: 1.28x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 760 us: 1.26x faster                                                       |
| pycparser                | 930 ms                                                      | 739 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.21 ms: 1.23x faster                                                      |
| thrift                   | 617 us                                                      | 505 us: 1.22x faster                                                       |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 57.2 ms: 1.16x faster                                                      |
| fannkuch                 | 256 ms                                                      | 220 ms: 1.16x faster                                                       |
| logging_format           | 6.76 us                                                     | 5.94 us: 1.14x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.0 ms: 1.14x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.53 us: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.7 ms: 1.09x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.3 ms: 1.05x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.70 us: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.86 us: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.49 us: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.3 ms: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 903 us: 1.13x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 70.6 ms: 1.14x slower                                                      |
| coverage                 | 39.0 ms                                                     | 44.4 ms: 1.14x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.49 ms: 1.14x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (3): pathlib, json_loads, pickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown