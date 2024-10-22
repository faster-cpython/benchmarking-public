# Results vs. 3.10.4

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-amd64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 43.1 ms: 1.19x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.2 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 580 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 59.7 ms: 1.03x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 86.7 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_compile  | 106 ms                                                      | 93.3 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.4 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.21x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.08 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 580 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| pylint                   | 350 ms                                                      | 227 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 62.8 ns: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.4 ms: 1.43x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| go                       | 139 ms                                                      | 99.7 ms: 1.39x faster                                                      |
| raytrace                 | 273 ms                                                      | 197 ms: 1.39x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 538 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 899 us: 1.35x faster                                                       |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.9 ms: 1.32x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.49 ms: 1.28x faster                                                      |
| pyflate                  | 409 ms                                                      | 320 ms: 1.28x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.08 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.69 sec: 1.25x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 51.5 ms: 1.21x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.21x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.21x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 804 us: 1.19x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 43.1 ms: 1.19x faster                                                      |
| scimark_sor              | 106 ms                                                      | 89.7 ms: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                      |
| thrift                   | 617 us                                                      | 529 us: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.2 ms: 1.16x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 44.1 ms: 1.14x faster                                                      |
| regex_compile            | 106 ms                                                      | 93.3 ms: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.6 ms: 1.13x faster                                                      |
| pycparser                | 930 ms                                                      | 833 ms: 1.12x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.7 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 71.3 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.6 ms: 1.08x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.16 sec: 1.05x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 571 ms: 1.04x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                                     |
| float                    | 61.7 ms                                                     | 59.7 ms: 1.03x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.0 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.3 ms: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.03x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.91 ms: 1.07x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 81.0 ms: 1.07x slower                                                      |
| async_generators         | 222 ms                                                      | 242 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 893 us: 1.12x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.7 ms: 1.12x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.4 ms: 1.13x slower                                                      |
| scimark_fft              | 187 ms                                                      | 213 ms: 1.14x slower                                                       |
| fannkuch                 | 256 ms                                                      | 292 ms: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                      |
| nbody                    | 71.3 ms                                                     | 86.7 ms: 1.22x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.98 ms: 1.26x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown