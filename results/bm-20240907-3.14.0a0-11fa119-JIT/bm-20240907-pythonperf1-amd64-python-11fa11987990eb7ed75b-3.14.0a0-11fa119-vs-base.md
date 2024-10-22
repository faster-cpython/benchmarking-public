# Results vs. base

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.04x faster
- HPT reliability: 90.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                                                               | 241 ms: 1.06x slower                                                                                                     |
| docutils       | 1.70 sec                                                                                                             | 1.91 sec: 1.13x slower                                                                                                   |
| html5lib       | 39.9 ms                                                                                                              | 42.0 ms: 1.05x slower                                                                                                    |
| tornado_http   | 93.8 ms                                                                                                              | 97.7 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.07x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none         | 217 ms                                                                                                               | 201 ms: 1.08x faster                                                                                                     |
| async_tree_io           | 613 ms                                                                                                               | 584 ms: 1.05x faster                                                                                                     |
| coroutines              | 14.1 ms                                                                                                              | 13.8 ms: 1.03x faster                                                                                                    |
| async_tree_io_tg        | 541 ms                                                                                                               | 555 ms: 1.03x slower                                                                                                     |
| async_tree_cpu_io_mixed | 383 ms                                                                                                               | 393 ms: 1.03x slower                                                                                                     |
| async_generators        | 249 ms                                                                                                               | 264 ms: 1.06x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization, asyncio_tcp, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 84.6 ms                                                                                                              | 49.0 ms: 1.73x faster                                                                                                    |
| float          | 57.2 ms                                                                                                              | 43.8 ms: 1.31x faster                                                                                                    |
| pidigits       | 152 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.32x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 15.1 ms                                                                                                              | 15.2 ms: 1.01x slower                                                                                                    |
| regex_effbot   | 1.58 ms                                                                                                              | 1.62 ms: 1.02x slower                                                                                                    |
| regex_dna      | 120 ms                                                                                                               | 124 ms: 1.03x slower                                                                                                     |
| regex_compile  | 90.8 ms                                                                                                              | 95.2 ms: 1.05x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.60 sec                                                                                                             | 1.24 sec: 1.29x faster                                                                                                   |
| xml_etree_generate   | 58.4 ms                                                                                                              | 49.0 ms: 1.19x faster                                                                                                    |
| xml_etree_process    | 41.2 ms                                                                                                              | 34.7 ms: 1.19x faster                                                                                                    |
| pickle_pure_python   | 213 us                                                                                                               | 194 us: 1.10x faster                                                                                                     |
| pickle_dict          | 19.0 us                                                                                                              | 17.7 us: 1.07x faster                                                                                                    |
| unpickle_pure_python | 150 us                                                                                                               | 141 us: 1.06x faster                                                                                                     |
| xml_etree_iterparse  | 65.3 ms                                                                                                              | 61.5 ms: 1.06x faster                                                                                                    |
| json_dumps           | 6.21 ms                                                                                                              | 5.86 ms: 1.06x faster                                                                                                    |
| unpickle             | 9.64 us                                                                                                              | 9.18 us: 1.05x faster                                                                                                    |
| pickle_list          | 2.99 us                                                                                                              | 2.87 us: 1.04x faster                                                                                                    |
| pickle               | 7.44 us                                                                                                              | 7.17 us: 1.04x faster                                                                                                    |
| xml_etree_parse      | 94.3 ms                                                                                                              | 92.6 ms: 1.02x faster                                                                                                    |
| unpickle_list        | 2.78 us                                                                                                              | 2.80 us: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                                                                              | 18.5 ms: 1.02x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.85 ms                                                                                                              | 5.15 ms: 1.33x faster                                                                                                    |
| django_template | 24.9 ms                                                                                                              | 26.1 ms: 1.05x slower                                                                                                    |
| genshi_text     | 17.1 ms                                                                                                              | 18.7 ms: 1.09x slower                                                                                                    |
| genshi_xml      | 36.6 ms                                                                                                              | 44.0 ms: 1.20x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.01x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 84.6 ms                                                                                                              | 49.0 ms: 1.73x faster                                                                                                    |
| scimark_sor              | 91.5 ms                                                                                                              | 59.9 ms: 1.53x faster                                                                                                    |
| spectral_norm            | 69.0 ms                                                                                                              | 45.6 ms: 1.51x faster                                                                                                    |
| scimark_fft              | 205 ms                                                                                                               | 148 ms: 1.39x faster                                                                                                     |
| deepcopy_memo            | 20.3 us                                                                                                              | 15.2 us: 1.34x faster                                                                                                    |
| mako                     | 6.85 ms                                                                                                              | 5.15 ms: 1.33x faster                                                                                                    |
| scimark_sparse_mat_mult  | 2.79 ms                                                                                                              | 2.12 ms: 1.31x faster                                                                                                    |
| float                    | 57.2 ms                                                                                                              | 43.8 ms: 1.31x faster                                                                                                    |
| tomli_loads              | 1.60 sec                                                                                                             | 1.24 sec: 1.29x faster                                                                                                   |
| fannkuch                 | 291 ms                                                                                                               | 232 ms: 1.25x faster                                                                                                     |
| crypto_pyaes             | 47.8 ms                                                                                                              | 38.3 ms: 1.25x faster                                                                                                    |
| scimark_lu               | 64.7 ms                                                                                                              | 52.3 ms: 1.24x faster                                                                                                    |
| deltablue                | 2.26 ms                                                                                                              | 1.83 ms: 1.23x faster                                                                                                    |
| pyflate                  | 321 ms                                                                                                               | 261 ms: 1.23x faster                                                                                                     |
| scimark_monte_carlo      | 50.4 ms                                                                                                              | 42.1 ms: 1.20x faster                                                                                                    |
| xml_etree_generate       | 58.4 ms                                                                                                              | 49.0 ms: 1.19x faster                                                                                                    |
| xml_etree_process        | 41.2 ms                                                                                                              | 34.7 ms: 1.19x faster                                                                                                    |
| comprehensions           | 11.9 us                                                                                                              | 10.6 us: 1.12x faster                                                                                                    |
| telco                    | 5.12 ms                                                                                                              | 4.64 ms: 1.10x faster                                                                                                    |
| pickle_pure_python       | 213 us                                                                                                               | 194 us: 1.10x faster                                                                                                     |
| pprint_safe_repr         | 549 ms                                                                                                               | 503 ms: 1.09x faster                                                                                                     |
| logging_silent           | 62.5 ns                                                                                                              | 57.3 ns: 1.09x faster                                                                                                    |
| pycparser                | 767 ms                                                                                                               | 706 ms: 1.09x faster                                                                                                     |
| pprint_pformat           | 1.12 sec                                                                                                             | 1.03 sec: 1.08x faster                                                                                                   |
| async_tree_none          | 217 ms                                                                                                               | 201 ms: 1.08x faster                                                                                                     |
| pickle_dict              | 19.0 us                                                                                                              | 17.7 us: 1.07x faster                                                                                                    |
| json                     | 3.16 ms                                                                                                              | 2.97 ms: 1.07x faster                                                                                                    |
| unpickle_pure_python     | 150 us                                                                                                               | 141 us: 1.06x faster                                                                                                     |
| xml_etree_iterparse      | 65.3 ms                                                                                                              | 61.5 ms: 1.06x faster                                                                                                    |
| chaos                    | 43.0 ms                                                                                                              | 40.6 ms: 1.06x faster                                                                                                    |
| json_dumps               | 6.21 ms                                                                                                              | 5.86 ms: 1.06x faster                                                                                                    |
| nqueens                  | 63.8 ms                                                                                                              | 60.5 ms: 1.05x faster                                                                                                    |
| meteor_contest           | 79.0 ms                                                                                                              | 75.1 ms: 1.05x faster                                                                                                    |
| deepcopy_reduce          | 1.89 us                                                                                                              | 1.80 us: 1.05x faster                                                                                                    |
| unpickle                 | 9.64 us                                                                                                              | 9.18 us: 1.05x faster                                                                                                    |
| async_tree_io            | 613 ms                                                                                                               | 584 ms: 1.05x faster                                                                                                     |
| logging_simple           | 6.23 us                                                                                                              | 5.97 us: 1.04x faster                                                                                                    |
| typing_runtime_protocols | 113 us                                                                                                               | 108 us: 1.04x faster                                                                                                     |
| pickle_list              | 2.99 us                                                                                                              | 2.87 us: 1.04x faster                                                                                                    |
| pickle                   | 7.44 us                                                                                                              | 7.17 us: 1.04x faster                                                                                                    |
| logging_format           | 6.64 us                                                                                                              | 6.43 us: 1.03x faster                                                                                                    |
| coroutines               | 14.1 ms                                                                                                              | 13.8 ms: 1.03x faster                                                                                                    |
| dulwich_log              | 44.1 ms                                                                                                              | 43.0 ms: 1.03x faster                                                                                                    |
| sqlite_synth             | 1.62 us                                                                                                              | 1.59 us: 1.02x faster                                                                                                    |
| xml_etree_parse          | 94.3 ms                                                                                                              | 92.6 ms: 1.02x faster                                                                                                    |
| sqlglot_parse            | 892 us                                                                                                               | 883 us: 1.01x faster                                                                                                     |
| pidigits                 | 152 ms                                                                                                               | 150 ms: 1.01x faster                                                                                                     |
| coverage                 | 48.6 ms                                                                                                              | 48.2 ms: 1.01x faster                                                                                                    |
| deepcopy                 | 189 us                                                                                                               | 188 us: 1.01x faster                                                                                                     |
| regex_v8                 | 15.1 ms                                                                                                              | 15.2 ms: 1.01x slower                                                                                                    |
| unpickle_list            | 2.78 us                                                                                                              | 2.80 us: 1.01x slower                                                                                                    |
| gc_traversal             | 1.55 ms                                                                                                              | 1.56 ms: 1.01x slower                                                                                                    |
| create_gc_cycles         | 902 us                                                                                                               | 914 us: 1.01x slower                                                                                                     |
| mdp                      | 1.47 sec                                                                                                             | 1.49 sec: 1.02x slower                                                                                                   |
| regex_effbot             | 1.58 ms                                                                                                              | 1.62 ms: 1.02x slower                                                                                                    |
| python_startup_no_site   | 18.1 ms                                                                                                              | 18.5 ms: 1.02x slower                                                                                                    |
| async_tree_io_tg         | 541 ms                                                                                                               | 555 ms: 1.03x slower                                                                                                     |
| async_tree_cpu_io_mixed  | 383 ms                                                                                                               | 393 ms: 1.03x slower                                                                                                     |
| raytrace                 | 191 ms                                                                                                               | 196 ms: 1.03x slower                                                                                                     |
| regex_dna                | 120 ms                                                                                                               | 124 ms: 1.03x slower                                                                                                     |
| sqlglot_transpile        | 1.10 ms                                                                                                              | 1.15 ms: 1.04x slower                                                                                                    |
| tornado_http             | 93.8 ms                                                                                                              | 97.7 ms: 1.04x slower                                                                                                    |
| django_template          | 24.9 ms                                                                                                              | 26.1 ms: 1.05x slower                                                                                                    |
| regex_compile            | 90.8 ms                                                                                                              | 95.2 ms: 1.05x slower                                                                                                    |
| go                       | 86.9 ms                                                                                                              | 91.4 ms: 1.05x slower                                                                                                    |
| html5lib                 | 39.9 ms                                                                                                              | 42.0 ms: 1.05x slower                                                                                                    |
| sqlglot_normalize        | 190 ms                                                                                                               | 200 ms: 1.05x slower                                                                                                     |
| bench_mp_pool            | 67.8 ms                                                                                                              | 71.6 ms: 1.06x slower                                                                                                    |
| async_generators         | 249 ms                                                                                                               | 264 ms: 1.06x slower                                                                                                     |
| 2to3                     | 227 ms                                                                                                               | 241 ms: 1.06x slower                                                                                                     |
| sympy_str                | 177 ms                                                                                                               | 188 ms: 1.06x slower                                                                                                     |
| richards_super           | 36.1 ms                                                                                                              | 38.4 ms: 1.07x slower                                                                                                    |
| sympy_expand             | 307 ms                                                                                                               | 329 ms: 1.07x slower                                                                                                     |
| sympy_sum                | 91.1 ms                                                                                                              | 97.8 ms: 1.07x slower                                                                                                    |
| generators               | 20.9 ms                                                                                                              | 22.8 ms: 1.09x slower                                                                                                    |
| genshi_text              | 17.1 ms                                                                                                              | 18.7 ms: 1.09x slower                                                                                                    |
| hexiom                   | 4.50 ms                                                                                                              | 4.92 ms: 1.09x slower                                                                                                    |
| sqlglot_optimize         | 36.2 ms                                                                                                              | 39.8 ms: 1.10x slower                                                                                                    |
| richards                 | 32.1 ms                                                                                                              | 35.8 ms: 1.11x slower                                                                                                    |
| sympy_integrate          | 13.1 ms                                                                                                              | 14.8 ms: 1.13x slower                                                                                                    |
| docutils                 | 1.70 sec                                                                                                             | 1.91 sec: 1.13x slower                                                                                                   |
| pylint                   | 226 ms                                                                                                               | 266 ms: 1.18x slower                                                                                                     |
| genshi_xml               | 36.6 ms                                                                                                              | 44.0 ms: 1.20x slower                                                                                                    |
| unpack_sequence          | 40.3 ns                                                                                                              | 58.4 ns: 1.45x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_memoization, asyncio_tcp, json_loads, python_startup, bench_thread_pool, pathlib, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, thrift, asyncio_tcp_ssl

# HPT report

- Reliability score: 90.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown