# Results vs. 3.10.4

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: windows-amd64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.06x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.67 ms: 1.24x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.43 sec: 1.27x slower                                                      |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| tornado_http   | 108 ms                                                      | 86.9 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 638 ms                                                      | 2.25 sec: 3.53x slower                                                      |
| async_tree_none         | 435 ms                                                      | 1.81 sec: 4.17x slower                                                      |
| async_tree_memoization  | 526 ms                                                      | 2.32 sec: 4.41x slower                                                      |
| async_tree_io           | 1.11 sec                                                    | 7.30 sec: 6.59x slower                                                      |
| Geometric mean          | (ref)                                                       | 4.55x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 58.4 ms: 1.22x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| float          | 61.7 ms                                                     | 81.6 ms: 1.32x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.8 ms: 1.28x faster                                                       |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 177 us: 1.53x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.39x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.6 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.59 us: 1.06x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 59.7 ms: 1.07x slower                                                       |
| pickle               | 6.85 us                                                     | 7.42 us: 1.08x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.00 us: 1.09x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.11x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 123 ms: 1.27x slower                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 94.3 ms: 1.45x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.9 ms: 1.16x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.6 ms: 1.39x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.58 ms: 1.62x faster                                                       |
| django_template | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.3 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 71.2 us: 4.72x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.58 ms: 1.62x faster                                                       |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.61x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 479 ms: 1.53x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 177 us: 1.53x faster                                                        |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 51.3 ms: 1.51x faster                                                       |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 840 us: 1.45x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 43.3 ms: 1.44x faster                                                       |
| go                       | 139 ms                                                      | 96.6 ms: 1.44x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.2 ms: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.39x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.35x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.35 ms: 1.32x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                       |
| scimark_sor              | 106 ms                                                      | 81.4 ms: 1.30x faster                                                       |
| regex_compile            | 106 ms                                                      | 82.8 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.66 sec: 1.27x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                       |
| tornado_http             | 108 ms                                                      | 86.9 ms: 1.25x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 983 ms: 1.24x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.67 ms: 1.24x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 479 ms: 1.24x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 69.5 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 86.7 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                       |
| nbody                    | 71.3 ms                                                     | 58.4 ms: 1.22x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.18x faster                                                       |
| deepcopy                 | 255 us                                                      | 221 us: 1.16x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 835 us: 1.15x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 181 ms: 1.13x faster                                                        |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                        |
| pycparser                | 930 ms                                                      | 828 ms: 1.12x faster                                                        |
| fannkuch                 | 256 ms                                                      | 228 ms: 1.12x faster                                                        |
| scimark_fft              | 187 ms                                                      | 168 ms: 1.12x faster                                                        |
| mypy2                    | 555 ms                                                      | 501 ms: 1.11x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.10x faster                                                       |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 37.3 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.86 ms: 1.10x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.6 ms: 1.09x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.37 us: 1.06x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.88 us: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| aiohttp                  | 995 us                                                      | 941 us: 1.06x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.59 us: 1.06x faster                                                       |
| create_gc_cycles         | 800 us                                                      | 757 us: 1.06x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                       |
| 2to3                     | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.37 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.5 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 77.1 ms: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 59.7 ms: 1.07x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.42 us: 1.08x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.00 us: 1.09x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.11x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 71.5 ms: 1.15x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.9 ms: 1.16x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 46.7 ns: 1.18x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.74 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                       |
| docutils                 | 1.92 sec                                                    | 2.43 sec: 1.27x slower                                                      |
| async_generators         | 222 ms                                                      | 281 ms: 1.27x slower                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 123 ms: 1.27x slower                                                        |
| float                    | 61.7 ms                                                     | 81.6 ms: 1.32x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.6 ms: 1.39x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 94.3 ms: 1.45x slower                                                       |
| pylint                   | 350 ms                                                      | 573 ms: 1.64x slower                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 2.25 sec: 3.53x slower                                                      |
| async_tree_none          | 435 ms                                                      | 1.81 sec: 4.17x slower                                                      |
| async_tree_memoization   | 526 ms                                                      | 2.32 sec: 4.41x slower                                                      |
| async_tree_io            | 1.11 sec                                                    | 7.30 sec: 6.59x slower                                                      |
| thrift                   | 617 us                                                      | 8.90 ms: 14.42x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: unknown