# Results vs. 3.10.4

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: windows-amd64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.1 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 250 ms: 2.10x faster                                                       |
| async_tree_none         | 435 ms                                                      | 207 ms: 2.10x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 530 ms: 2.09x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 381 ms: 1.68x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.98x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.3 ms: 1.14x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 75.2 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.0 ms: 1.25x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 193 us: 1.39x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 38.5 ms: 1.16x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.0 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 22.9 ms: 1.26x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.8 ms: 1.21x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 250 ms: 2.10x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.99 ms: 2.10x faster                                                      |
| async_tree_none          | 435 ms                                                      | 207 ms: 2.10x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 530 ms: 2.09x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 381 ms: 1.68x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.1 ns: 1.66x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.66x faster                                                      |
| raytrace                 | 273 ms                                                      | 169 ms: 1.62x faster                                                       |
| pylint                   | 350 ms                                                      | 219 ms: 1.60x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                                      |
| go                       | 139 ms                                                      | 88.1 ms: 1.58x faster                                                      |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.52x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 59.4 ms: 1.45x faster                                                      |
| deepcopy                 | 255 us                                                      | 177 us: 1.44x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 843 us: 1.44x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.98 ms: 1.44x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.41x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 193 us: 1.39x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 528 ms: 1.39x faster                                                       |
| pyflate                  | 409 ms                                                      | 299 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.7 ms: 1.31x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.63 sec: 1.29x faster                                                     |
| scimark_sor              | 106 ms                                                      | 83.0 ms: 1.28x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template          | 28.9 ms                                                     | 22.9 ms: 1.26x faster                                                      |
| regex_compile            | 106 ms                                                      | 85.0 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.0 ms: 1.22x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.8 ms: 1.21x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 793 us: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.1 ms: 1.19x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 33.6 ms: 1.18x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.6 ms: 1.18x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.5 ms: 1.16x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 178 ms: 1.15x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 67.8 ms: 1.14x faster                                                      |
| float                    | 61.7 ms                                                     | 54.3 ms: 1.14x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 528 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                                      |
| pycparser                | 930 ms                                                      | 852 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.33 us: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.88 us: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.0 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                                      |
| nbody                    | 71.3 ms                                                     | 75.2 ms: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.91 ms: 1.07x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.4 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| scimark_fft              | 187 ms                                                      | 207 ms: 1.10x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 899 us: 1.12x slower                                                       |
| fannkuch                 | 256 ms                                                      | 290 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown