
# Results vs. 3.10.4

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 335 ms: 1.00x faster                                     |
| docutils       | 3.19 sec                                                            | 3.22 sec: 1.01x slower                                   |
| Geometric mean | (ref)                                                               | 1.01x slower                                             |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 146 ms                                                              | 137 ms: 1.06x faster                                     |
| float          | 110 ms                                                              | 109 ms: 1.01x faster                                     |
| pidigits       | 190 ms                                                              | 189 ms: 1.01x faster                                     |
| Geometric mean | (ref)                                                               | 1.03x faster                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_v8       | 24.9 ms                                                             | 24.1 ms: 1.03x faster                                    |
| regex_compile  | 177 ms                                                              | 177 ms: 1.00x faster                                     |
| regex_dna      | 213 ms                                                              | 216 ms: 1.02x slower                                     |
| regex_effbot   | 3.22 ms                                                             | 3.62 ms: 1.12x slower                                    |
| Geometric mean | (ref)                                                               | 1.02x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_list          | 4.73 us                                                             | 4.17 us: 1.13x faster                                    |
| xml_etree_generate   | 94.9 ms                                                             | 93.0 ms: 1.02x faster                                    |
| pickle_pure_python   | 457 us                                                              | 449 us: 1.02x faster                                     |
| xml_etree_parse      | 164 ms                                                              | 161 ms: 1.02x faster                                     |
| unpickle_pure_python | 300 us                                                              | 297 us: 1.01x faster                                     |
| xml_etree_iterparse  | 111 ms                                                              | 110 ms: 1.01x faster                                     |
| json_dumps           | 13.7 ms                                                             | 13.6 ms: 1.01x faster                                    |
| xml_etree_process    | 74.8 ms                                                             | 74.4 ms: 1.00x faster                                    |
| pickle_dict          | 27.8 us                                                             | 30.5 us: 1.10x slower                                    |
| Geometric mean       | (ref)                                                               | 1.01x faster                                             |

Benchmark hidden because not significant (4): unpickle, json_loads, unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.33 ms: 1.52x faster                                    |
| python_startup_no_site | 5.80 ms                                                             | 5.79 ms: 1.00x faster                                    |
| Geometric mean         | (ref)                                                               | 1.23x faster                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 64.3 ms                                                             | 62.6 ms: 1.03x faster                                    |
| genshi_text     | 30.4 ms                                                             | 30.1 ms: 1.01x faster                                    |
| mako            | 14.7 ms                                                             | 14.6 ms: 1.01x faster                                    |
| django_template | 45.8 ms                                                             | 46.6 ms: 1.02x slower                                    |
| Geometric mean  | (ref)                                                               | 1.01x faster                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup          | 14.1 ms                                                             | 9.33 ms: 1.52x faster                                    |
| pickle_list             | 4.73 us                                                             | 4.17 us: 1.13x faster                                    |
| nbody                   | 146 ms                                                              | 137 ms: 1.06x faster                                     |
| spectral_norm           | 150 ms                                                              | 143 ms: 1.05x faster                                     |
| aiohttp                 | 1.35 ms                                                             | 1.29 ms: 1.04x faster                                    |
| scimark_fft             | 425 ms                                                              | 408 ms: 1.04x faster                                     |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 5.39 ms: 1.04x faster                                    |
| fannkuch                | 485 ms                                                              | 467 ms: 1.04x faster                                     |
| bench_thread_pool       | 954 us                                                              | 919 us: 1.04x faster                                     |
| coroutines              | 31.8 ms                                                             | 30.6 ms: 1.04x faster                                    |
| deepcopy_memo           | 51.8 us                                                             | 49.9 us: 1.04x faster                                    |
| scimark_monte_carlo     | 109 ms                                                              | 105 ms: 1.03x faster                                     |
| regex_v8                | 24.9 ms                                                             | 24.1 ms: 1.03x faster                                    |
| gunicorn                | 1.43 ms                                                             | 1.39 ms: 1.03x faster                                    |
| genshi_xml              | 64.3 ms                                                             | 62.6 ms: 1.03x faster                                    |
| unpack_sequence         | 65.6 ns                                                             | 64.0 ns: 1.03x faster                                    |
| scimark_sor             | 198 ms                                                              | 193 ms: 1.02x faster                                     |
| deepcopy                | 438 us                                                              | 428 us: 1.02x faster                                     |
| richards                | 74.2 ms                                                             | 72.6 ms: 1.02x faster                                    |
| sqlglot_parse           | 2.07 ms                                                             | 2.03 ms: 1.02x faster                                    |
| xml_etree_generate      | 94.9 ms                                                             | 93.0 ms: 1.02x faster                                    |
| pickle_pure_python      | 457 us                                                              | 449 us: 1.02x faster                                     |
| pyflate                 | 671 ms                                                              | 659 ms: 1.02x faster                                     |
| xml_etree_parse         | 164 ms                                                              | 161 ms: 1.02x faster                                     |
| sqlglot_transpile       | 2.45 ms                                                             | 2.41 ms: 1.02x faster                                    |
| raytrace                | 470 ms                                                              | 463 ms: 1.02x faster                                     |
| meteor_contest          | 115 ms                                                              | 113 ms: 1.02x faster                                     |
| crypto_pyaes            | 117 ms                                                              | 115 ms: 1.02x faster                                     |
| dulwich_log             | 76.3 ms                                                             | 75.4 ms: 1.01x faster                                    |
| genshi_text             | 30.4 ms                                                             | 30.1 ms: 1.01x faster                                    |
| hexiom                  | 9.50 ms                                                             | 9.42 ms: 1.01x faster                                    |
| unpickle_pure_python    | 300 us                                                              | 297 us: 1.01x faster                                     |
| mako                    | 14.7 ms                                                             | 14.6 ms: 1.01x faster                                    |
| float                   | 110 ms                                                              | 109 ms: 1.01x faster                                     |
| asyncio_tcp             | 922 ms                                                              | 915 ms: 1.01x faster                                     |
| xml_etree_iterparse     | 111 ms                                                              | 110 ms: 1.01x faster                                     |
| json_dumps              | 13.7 ms                                                             | 13.6 ms: 1.01x faster                                    |
| mypy2                   | 432 ms                                                              | 429 ms: 1.01x faster                                     |
| pidigits                | 190 ms                                                              | 189 ms: 1.01x faster                                     |
| xml_etree_process       | 74.8 ms                                                             | 74.4 ms: 1.00x faster                                    |
| create_gc_cycles        | 1.64 ms                                                             | 1.63 ms: 1.00x faster                                    |
| regex_compile           | 177 ms                                                              | 177 ms: 1.00x faster                                     |
| 2to3                    | 336 ms                                                              | 335 ms: 1.00x faster                                     |
| python_startup_no_site  | 5.80 ms                                                             | 5.79 ms: 1.00x faster                                    |
| sympy_integrate         | 24.3 ms                                                             | 24.4 ms: 1.00x slower                                    |
| gc_traversal            | 3.53 ms                                                             | 3.54 ms: 1.00x slower                                    |
| sympy_str               | 328 ms                                                              | 329 ms: 1.00x slower                                     |
| chaos                   | 106 ms                                                              | 106 ms: 1.00x slower                                     |
| generators              | 75.7 ms                                                             | 76.1 ms: 1.01x slower                                    |
| sqlalchemy_declarative  | 166 ms                                                              | 167 ms: 1.01x slower                                     |
| pylint                  | 521 ms                                                              | 524 ms: 1.01x slower                                     |
| docutils                | 3.19 sec                                                            | 3.22 sec: 1.01x slower                                   |
| sqlglot_normalize       | 135 ms                                                              | 136 ms: 1.01x slower                                     |
| sympy_expand            | 540 ms                                                              | 546 ms: 1.01x slower                                     |
| coverage                | 70.6 ms                                                             | 71.5 ms: 1.01x slower                                    |
| async_generators        | 420 ms                                                              | 426 ms: 1.01x slower                                     |
| nqueens                 | 98.8 ms                                                             | 100 ms: 1.01x slower                                     |
| logging_format          | 9.07 us                                                             | 9.20 us: 1.01x slower                                    |
| regex_dna               | 213 ms                                                              | 216 ms: 1.02x slower                                     |
| deltablue               | 7.30 ms                                                             | 7.41 ms: 1.02x slower                                    |
| django_template         | 45.8 ms                                                             | 46.6 ms: 1.02x slower                                    |
| sympy_sum               | 185 ms                                                              | 189 ms: 1.02x slower                                     |
| pprint_pformat          | 1.98 sec                                                            | 2.02 sec: 1.02x slower                                   |
| pprint_safe_repr        | 953 ms                                                              | 975 ms: 1.02x slower                                     |
| logging_simple          | 8.21 us                                                             | 8.41 us: 1.02x slower                                    |
| mdp                     | 2.75 sec                                                            | 2.82 sec: 1.02x slower                                   |
| logging_silent          | 169 ns                                                              | 174 ns: 1.03x slower                                     |
| async_tree_cpu_io_mixed | 944 ms                                                              | 997 ms: 1.06x slower                                     |
| pickle_dict             | 27.8 us                                                             | 30.5 us: 1.10x slower                                    |
| regex_effbot            | 3.22 ms                                                             | 3.62 ms: 1.12x slower                                    |
| Geometric mean          | (ref)                                                               | 1.01x faster                                             |

Benchmark hidden because not significant (25): sqlalchemy_imperative, unpickle, dask, pathlib, json, json_loads, thrift, unpickle_list, flaskblogging, sqlite_synth, pickle, chameleon, bench_mp_pool, scimark_lu, async_tree_io, sqlglot_optimize, go, deepcopy_reduce, async_tree_memoization, pycparser, telco, tornado_http, djangocms, async_tree_none, html5lib
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: comprehensions
