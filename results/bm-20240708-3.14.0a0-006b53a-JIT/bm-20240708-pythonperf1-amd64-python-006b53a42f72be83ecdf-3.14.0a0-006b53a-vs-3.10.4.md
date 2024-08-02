# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-amd64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                      |
| tornado_http   | 108 ms                                                      | 86.3 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 522 ms: 2.13x faster                                                       |
| async_tree_none         | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 249 ms: 2.12x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.00x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.7 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.0 ms: 1.19x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 18.2 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 176 us: 1.54x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.6 ms: 1.07x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 43.7 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 522 ms: 2.13x faster                                                       |
| async_tree_none          | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 249 ms: 2.12x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 15.6 us: 1.85x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.2 ms: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.9 ns: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                      |
| pyflate                  | 409 ms                                                      | 262 ms: 1.56x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 176 us: 1.54x faster                                                       |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.6 ms: 1.52x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 800 us: 1.52x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| richards_super           | 52.2 ms                                                     | 35.1 ms: 1.49x faster                                                      |
| go                       | 139 ms                                                      | 93.4 ms: 1.49x faster                                                      |
| deepcopy                 | 255 us                                                      | 175 us: 1.46x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.02 ms: 1.44x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                       |
| generators               | 32.4 ms                                                     | 23.4 ms: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.0 ms: 1.37x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.7 ms: 1.35x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 957 ms: 1.27x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 465 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                      |
| tornado_http             | 108 ms                                                      | 86.3 ms: 1.26x faster                                                      |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.65 ms: 1.24x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.22x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 798 us: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.0 ms: 1.19x faster                                                      |
| scimark_sor              | 106 ms                                                      | 89.5 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 73.0 ms: 1.18x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                      |
| sympy_sum                | 107 ms                                                      | 92.2 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| pycparser                | 930 ms                                                      | 809 ms: 1.15x faster                                                       |
| fannkuch                 | 256 ms                                                      | 226 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.4 ms: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.1 ms: 1.11x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.21 us: 1.09x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.77 us: 1.08x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.6 ms: 1.07x faster                                                      |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.0 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.3 ms: 1.02x faster                                                      |
| python_startup           | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 43.7 ms: 1.06x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.4 ms: 1.12x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.42 ms: 1.12x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 900 us: 1.13x slower                                                       |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 18.2 ms: 1.18x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.2 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown