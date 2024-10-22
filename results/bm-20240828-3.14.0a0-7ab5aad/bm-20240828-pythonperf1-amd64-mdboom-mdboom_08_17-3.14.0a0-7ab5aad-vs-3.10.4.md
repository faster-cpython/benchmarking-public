# Results vs. 3.10.4

- fork: mdboom
- ref: mdboom_08_17
- machine: windows-amd64
- commit hash: 7ab5aad
- commit date: 2024-08-28
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                               |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                             |
| html5lib       | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                              |
| tornado_http   | 108 ms                                                      | 93.5 ms: 1.16x faster                                              |
| Geometric mean | (ref)                                                       | 1.13x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                               |
| async_tree_memoization  | 526 ms                                                      | 267 ms: 1.97x faster                                               |
| async_tree_io           | 1.11 sec                                                    | 581 ms: 1.91x faster                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                               |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.1 ms: 1.10x faster                                              |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                               |
| nbody          | 71.3 ms                                                     | 85.1 ms: 1.19x slower                                              |
| Geometric mean | (ref)                                                       | 1.03x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.4 ms: 1.17x faster                                              |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                               |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                              |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                       | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.08 ms: 1.51x faster                                              |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.29x faster                                               |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                               |
| xml_etree_process    | 44.5 ms                                                     | 40.2 ms: 1.11x faster                                              |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                             |
| xml_etree_parse      | 96.8 ms                                                     | 96.0 ms: 1.01x faster                                              |
| xml_etree_generate   | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                              |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                              |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                              |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.98 ms: 1.29x faster                                              |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                              |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                              |
| genshi_xml      | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                              |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                               |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                               |
| async_tree_memoization   | 526 ms                                                      | 267 ms: 1.97x faster                                               |
| async_tree_io            | 1.11 sec                                                    | 581 ms: 1.91x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                               |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                              |
| pylint                   | 350 ms                                                      | 227 ms: 1.55x faster                                               |
| json_dumps               | 9.16 ms                                                     | 6.08 ms: 1.51x faster                                              |
| logging_silent           | 94.6 ns                                                     | 62.9 ns: 1.50x faster                                              |
| raytrace                 | 273 ms                                                      | 187 ms: 1.46x faster                                               |
| go                       | 139 ms                                                      | 97.6 ms: 1.42x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                              |
| chaos                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                              |
| richards_super           | 52.2 ms                                                     | 37.7 ms: 1.39x faster                                              |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                              |
| sqlglot_parse            | 1.22 ms                                                     | 889 us: 1.37x faster                                               |
| asyncio_tcp              | 732 ms                                                      | 539 ms: 1.36x faster                                               |
| scimark_lu               | 85.8 ms                                                     | 63.3 ms: 1.36x faster                                              |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                               |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                              |
| hexiom                   | 5.74 ms                                                     | 4.36 ms: 1.32x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                              |
| mako                     | 9.03 ms                                                     | 6.98 ms: 1.29x faster                                              |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.29x faster                                               |
| richards                 | 42.4 ms                                                     | 33.3 ms: 1.27x faster                                              |
| pyflate                  | 409 ms                                                      | 325 ms: 1.26x faster                                               |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.68 sec: 1.26x faster                                             |
| mdp                      | 1.78 sec                                                    | 1.42 sec: 1.26x faster                                             |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                               |
| html5lib                 | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                              |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                               |
| sympy_sum                | 107 ms                                                      | 90.8 ms: 1.18x faster                                              |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                              |
| regex_compile            | 106 ms                                                      | 90.4 ms: 1.17x faster                                              |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                               |
| tornado_http             | 108 ms                                                      | 93.5 ms: 1.16x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.5 ms: 1.16x faster                                              |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                              |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                              |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                               |
| scimark_sor              | 106 ms                                                      | 93.0 ms: 1.14x faster                                              |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                              |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 40.2 ms: 1.11x faster                                              |
| genshi_xml               | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 36.0 ms: 1.10x faster                                              |
| float                    | 61.7 ms                                                     | 56.1 ms: 1.10x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                             |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                               |
| spectral_norm            | 77.3 ms                                                     | 71.3 ms: 1.08x faster                                              |
| pycparser                | 930 ms                                                      | 871 ms: 1.07x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 555 ms: 1.07x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                             |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                               |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                             |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                               |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                              |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                              |
| nqueens                  | 66.6 ms                                                     | 64.7 ms: 1.03x faster                                              |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                               |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.01x faster                                              |
| xml_etree_parse          | 96.8 ms                                                     | 96.0 ms: 1.01x faster                                              |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                               |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                              |
| meteor_contest           | 75.9 ms                                                     | 77.8 ms: 1.02x slower                                              |
| pathlib                  | 75.7 ms                                                     | 77.9 ms: 1.03x slower                                              |
| xml_etree_generate       | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.86 ms: 1.05x slower                                              |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                              |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                              |
| bench_mp_pool            | 62.0 ms                                                     | 68.4 ms: 1.10x slower                                              |
| scimark_fft              | 187 ms                                                      | 207 ms: 1.11x slower                                               |
| gc_traversal             | 1.41 ms                                                     | 1.58 ms: 1.12x slower                                              |
| create_gc_cycles         | 800 us                                                      | 908 us: 1.14x slower                                               |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                               |
| fannkuch                 | 256 ms                                                      | 297 ms: 1.16x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                              |
| nbody                    | 71.3 ms                                                     | 85.1 ms: 1.19x slower                                              |
| telco                    | 3.94 ms                                                     | 4.99 ms: 1.27x slower                                              |
| coverage                 | 39.0 ms                                                     | 50.1 ms: 1.29x slower                                              |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, logging_format
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240828-3.14.0a0-7ab5aad/bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown