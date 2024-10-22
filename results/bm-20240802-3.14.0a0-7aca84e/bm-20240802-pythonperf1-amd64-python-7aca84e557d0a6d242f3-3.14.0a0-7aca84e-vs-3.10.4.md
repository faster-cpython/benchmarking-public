# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 236 ms: 1.04x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 95.3 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 223 ms: 1.96x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 270 ms: 1.95x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 597 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.84x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 57.0 ms: 1.08x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 85.4 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                       |
| regex_compile  | 106 ms                                                      | 94.5 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 221 us: 1.22x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.05x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.06 ms: 1.28x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.4 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.91x faster                                                       |
| async_tree_none          | 435 ms                                                      | 223 ms: 1.96x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 270 ms: 1.95x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 597 ms: 1.86x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| pylint                   | 350 ms                                                      | 232 ms: 1.51x faster                                                       |
| generators               | 32.4 ms                                                     | 21.8 ms: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.26 ms: 1.46x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 65.5 ns: 1.45x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.7 us: 1.39x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| go                       | 139 ms                                                      | 101 ms: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 903 us: 1.35x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.3 ms: 1.33x faster                                                      |
| raytrace                 | 273 ms                                                      | 206 ms: 1.33x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.8 ms: 1.32x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.06 ms: 1.28x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.67 sec: 1.27x faster                                                     |
| pyflate                  | 409 ms                                                      | 332 ms: 1.23x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.7 ms: 1.22x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.70 ms: 1.22x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 221 us: 1.22x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 52.0 ms: 1.20x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 637 ms: 1.15x faster                                                       |
| pycparser                | 930 ms                                                      | 811 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 837 us: 1.14x faster                                                       |
| sympy_sum                | 107 ms                                                      | 94.0 ms: 1.14x faster                                                      |
| tornado_http             | 108 ms                                                      | 95.3 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.4 ms: 1.14x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.5 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.12x faster                                                      |
| regex_compile            | 106 ms                                                      | 94.5 ms: 1.12x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| scimark_sor              | 106 ms                                                      | 95.8 ms: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.4 ms: 1.10x faster                                                      |
| float                    | 61.7 ms                                                     | 57.0 ms: 1.08x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                     |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.05x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 37.8 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                      |
| 2to3                     | 246 ms                                                      | 236 ms: 1.04x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 74.7 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.18 sec: 1.03x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 581 ms: 1.02x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.2 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.03x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.01 us: 1.04x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.52 us: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                      |
| scimark_fft              | 187 ms                                                      | 202 ms: 1.08x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 81.5 ms: 1.08x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.4 ms: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 912 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| fannkuch                 | 256 ms                                                      | 296 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 85.4 ms: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.13 ms: 1.30x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (2): sympy_expand, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown