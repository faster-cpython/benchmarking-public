# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-amd64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.174x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.2 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 92.2 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.08x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 574 ms: 1.93x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 82.0 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.6 ms: 1.04x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.27 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.95 us: 1.07x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.9 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.03 ms: 1.28x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                      |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.06x faster                                                       |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.08x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 574 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 85.9 ms: 1.62x faster                                                      |
| pylint                   | 350 ms                                                      | 223 ms: 1.57x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 62.3 ns: 1.52x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 526 ms: 1.39x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 885 us: 1.37x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.37x faster                                                      |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                       |
| raytrace                 | 273 ms                                                      | 201 ms: 1.36x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.7 ms: 1.35x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.58 sec: 1.33x faster                                                     |
| richards                 | 42.4 ms                                                     | 32.0 ms: 1.33x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.43 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.03 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.27x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.2 ms: 1.25x faster                                                      |
| pyflate                  | 409 ms                                                      | 328 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 42.2 ms: 1.21x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 802 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                       |
| tornado_http             | 108 ms                                                      | 92.2 ms: 1.17x faster                                                      |
| scimark_sor              | 106 ms                                                      | 91.3 ms: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.4 ms: 1.16x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.5 ms: 1.16x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.5 ms: 1.16x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| float                    | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.08x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 546 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 71.5 ms: 1.08x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.0 ms: 1.03x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.7 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 39.3 ns: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.75 ms: 1.01x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.4 ms: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.4 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.6 ms: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.27 us: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.95 us: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.09x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.9 us: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 68.8 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 890 us: 1.11x slower                                                       |
| scimark_fft              | 187 ms                                                      | 209 ms: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| nbody                    | 71.3 ms                                                     | 82.0 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.0 ms: 1.18x slower                                                      |
| fannkuch                 | 256 ms                                                      | 305 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.89 ms: 1.24x slower                                                      |
| json                     | 3.14 ms                                                     | 4.33 ms: 1.38x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, logging_format
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.174x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown