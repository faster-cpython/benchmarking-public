
# Results vs. 3.10.4

- fork: python
- ref: 7c12e4835ebe52287acd
- machine: windows-amd64
- commit hash: 7c12e48
- commit date: 2021-10-05
- overall geometric mean: 1.02x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 222 ms: 1.07x faster                                                       |
| chameleon      | 5.92 ms                                                     | 5.68 ms: 1.04x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.73 sec: 1.10x faster                                                     |
| html5lib       | 46.5 ms                                                     | 41.5 ms: 1.12x faster                                                      |
| tornado_http   | 109 ms                                                      | 97.6 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 57.2 ms: 1.05x faster                                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.04x slower                                                       |
| nbody          | 69.3 ms                                                     | 86.8 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 92.3 ms: 1.12x faster                                                      |
| regex_v8       | 15.0 ms                                                     | 14.4 ms: 1.05x faster                                                      |
| regex_dna      | 132 ms                                                      | 129 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list       | 2.81 us                                                     | 2.56 us: 1.10x faster                                                      |
| unpickle            | 9.17 us                                                     | 8.48 us: 1.08x faster                                                      |
| xml_etree_process   | 43.4 ms                                                     | 40.3 ms: 1.08x faster                                                      |
| pickle_pure_python  | 257 us                                                      | 240 us: 1.07x faster                                                       |
| json_dumps          | 8.50 ms                                                     | 8.03 ms: 1.06x faster                                                      |
| xml_etree_parse     | 102 ms                                                      | 98.4 ms: 1.03x faster                                                      |
| pickle              | 6.80 us                                                     | 6.58 us: 1.03x faster                                                      |
| pickle_dict         | 16.9 us                                                     | 16.8 us: 1.01x faster                                                      |
| xml_etree_generate  | 54.5 ms                                                     | 54.8 ms: 1.01x slower                                                      |
| json_loads          | 14.2 us                                                     | 14.4 us: 1.02x slower                                                      |
| pickle_list         | 2.59 us                                                     | 2.66 us: 1.03x slower                                                      |
| xml_etree_iterparse | 63.5 ms                                                     | 65.6 ms: 1.03x slower                                                      |
| Geometric mean      | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 20.7 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                      |
| django_template | 28.2 ms                                                     | 25.8 ms: 1.09x faster                                                      |
| mako            | 8.80 ms                                                     | 8.12 ms: 1.08x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 37.8 ms: 1.07x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf1-amd64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 420 ms                                                      | 296 ms: 1.42x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 777 ms: 1.37x faster                                                       |
| deltablue               | 4.17 ms                                                     | 3.12 ms: 1.34x faster                                                      |
| async_tree_memoization  | 497 ms                                                      | 384 ms: 1.30x faster                                                       |
| go                      | 136 ms                                                      | 108 ms: 1.26x faster                                                       |
| raytrace                | 271 ms                                                      | 224 ms: 1.21x faster                                                       |
| richards                | 41.2 ms                                                     | 34.7 ms: 1.19x faster                                                      |
| logging_simple          | 6.20 us                                                     | 5.24 us: 1.18x faster                                                      |
| logging_format          | 6.66 us                                                     | 5.64 us: 1.18x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 83.4 ns: 1.16x faster                                                      |
| thrift                  | 615 us                                                      | 535 us: 1.15x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 628 ms: 1.13x faster                                                       |
| async_generators        | 224 ms                                                      | 198 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 541 ms: 1.13x faster                                                       |
| regex_compile           | 103 ms                                                      | 92.3 ms: 1.12x faster                                                      |
| html5lib                | 46.5 ms                                                     | 41.5 ms: 1.12x faster                                                      |
| tornado_http            | 109 ms                                                      | 97.6 ms: 1.12x faster                                                      |
| pycparser               | 868 ms                                                      | 777 ms: 1.12x faster                                                       |
| sqlalchemy_declarative  | 95.4 ms                                                     | 86.3 ms: 1.10x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                      |
| unpickle_list           | 2.81 us                                                     | 2.56 us: 1.10x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.73 sec: 1.10x faster                                                     |
| django_template         | 28.2 ms                                                     | 25.8 ms: 1.09x faster                                                      |
| generators              | 31.6 ms                                                     | 28.9 ms: 1.09x faster                                                      |
| pylint                  | 347 ms                                                      | 318 ms: 1.09x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.58 sec: 1.09x faster                                                     |
| mako                    | 8.80 ms                                                     | 8.12 ms: 1.08x faster                                                      |
| unpickle                | 9.17 us                                                     | 8.48 us: 1.08x faster                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 57.7 ms: 1.08x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 40.3 ms: 1.08x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 37.8 ms: 1.07x faster                                                      |
| chaos                   | 58.9 ms                                                     | 55.0 ms: 1.07x faster                                                      |
| hexiom                  | 5.52 ms                                                     | 5.17 ms: 1.07x faster                                                      |
| pickle_pure_python      | 257 us                                                      | 240 us: 1.07x faster                                                       |
| 2to3                    | 237 ms                                                      | 222 ms: 1.07x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| pyflate                 | 387 ms                                                      | 365 ms: 1.06x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 8.03 ms: 1.06x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 73.4 ms: 1.05x faster                                                      |
| float                   | 60.2 ms                                                     | 57.2 ms: 1.05x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 14.4 ms: 1.05x faster                                                      |
| chameleon               | 5.92 ms                                                     | 5.68 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.16 sec: 1.04x faster                                                     |
| sympy_sum               | 104 ms                                                      | 100 ms: 1.04x faster                                                       |
| dask                    | 305 ms                                                      | 295 ms: 1.03x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 98.4 ms: 1.03x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 915 us: 1.03x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 570 ms: 1.03x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.58 us: 1.03x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 46.1 ms: 1.03x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 14.4 ms: 1.03x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 37.8 ms: 1.03x faster                                                      |
| regex_dna               | 132 ms                                                      | 129 ms: 1.03x faster                                                       |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.7 ms: 1.02x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 83.6 ms: 1.02x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                      |
| sympy_expand            | 315 ms                                                      | 309 ms: 1.02x faster                                                       |
| json                    | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                      |
| pickle_dict             | 16.9 us                                                     | 16.8 us: 1.01x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 201 ms: 1.01x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 54.8 ms: 1.01x slower                                                      |
| nqueens                 | 67.0 ms                                                     | 67.7 ms: 1.01x slower                                                      |
| json_loads              | 14.2 us                                                     | 14.4 us: 1.02x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.37 ms: 1.02x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.66 us: 1.03x slower                                                      |
| create_gc_cycles        | 782 us                                                      | 807 us: 1.03x slower                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 65.6 ms: 1.03x slower                                                      |
| pidigits                | 145 ms                                                      | 150 ms: 1.04x slower                                                       |
| python_startup          | 20.0 ms                                                     | 20.7 ms: 1.04x slower                                                      |
| bench_mp_pool           | 60.7 ms                                                     | 63.0 ms: 1.04x slower                                                      |
| meteor_contest          | 72.5 ms                                                     | 75.3 ms: 1.04x slower                                                      |
| sqlglot_transpile       | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                                      |
| telco                   | 3.78 ms                                                     | 3.98 ms: 1.05x slower                                                      |
| sqlglot_parse           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| fannkuch                | 258 ms                                                      | 279 ms: 1.08x slower                                                       |
| spectral_norm           | 78.0 ms                                                     | 84.7 ms: 1.09x slower                                                      |
| unpack_sequence         | 37.8 ns                                                     | 41.7 ns: 1.10x slower                                                      |
| scimark_fft             | 193 ms                                                      | 216 ms: 1.12x slower                                                       |
| coroutines              | 15.9 ms                                                     | 17.9 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 3.18 ms: 1.20x slower                                                      |
| comprehensions          | 16.0 us                                                     | 19.1 us: 1.20x slower                                                      |
| nbody                   | 69.3 ms                                                     | 86.8 ms: 1.25x slower                                                      |
| coverage                | 40.0 ms                                                     | 261 ms: 6.53x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (9): sympy_str, regex_effbot, flaskblogging, deepcopy_memo, python_startup_no_site, unpickle_pure_python, scimark_sor, deepcopy, deepcopy_reduce
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
