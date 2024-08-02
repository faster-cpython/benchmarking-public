# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg | 936 ms                                                     | 902 ms: 1.04x faster                                                    |
| Geometric mean   | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                   |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                   |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                    |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                      | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 85.8 ms: 1.02x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                                  |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.01x slower                                                    |
| unpickle_list        | 5.34 us                                                    | 5.42 us: 1.01x slower                                                   |
| pickle_dict          | 34.8 us                                                    | 35.6 us: 1.02x slower                                                   |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (4): json_loads, pickle_pure_python, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                   |
| genshi_xml     | 51.6 ms                                                    | 52.0 ms: 1.01x slower                                                   |
| mako           | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| richards                | 50.9 ms                                                    | 47.7 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 4.94 ms: 1.07x faster                                                   |
| pathlib                 | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                   |
| richards_super          | 57.4 ms                                                    | 54.0 ms: 1.06x faster                                                   |
| crypto_pyaes            | 77.5 ms                                                    | 73.7 ms: 1.05x faster                                                   |
| logging_silent          | 105 ns                                                     | 99.6 ns: 1.05x faster                                                   |
| gc_traversal            | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                   |
| scimark_lu              | 122 ms                                                     | 117 ms: 1.04x faster                                                    |
| async_tree_io_tg        | 936 ms                                                     | 902 ms: 1.04x faster                                                    |
| scimark_fft             | 392 ms                                                     | 379 ms: 1.04x faster                                                    |
| spectral_norm           | 116 ms                                                     | 112 ms: 1.04x faster                                                    |
| dulwich_log             | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                   |
| chaos                   | 61.3 ms                                                    | 59.7 ms: 1.03x faster                                                   |
| create_gc_cycles        | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                   |
| xml_etree_process       | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                                   |
| xml_etree_parse         | 162 ms                                                     | 158 ms: 1.02x faster                                                    |
| pyflate                 | 484 ms                                                     | 474 ms: 1.02x faster                                                    |
| thrift                  | 823 us                                                     | 805 us: 1.02x faster                                                    |
| go                      | 145 ms                                                     | 142 ms: 1.02x faster                                                    |
| mdp                     | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                  |
| xml_etree_generate      | 87.4 ms                                                    | 85.8 ms: 1.02x faster                                                   |
| docutils                | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                  |
| genshi_text             | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                   |
| logging_format          | 6.47 us                                                    | 6.36 us: 1.02x faster                                                   |
| nqueens                 | 81.4 ms                                                    | 80.2 ms: 1.01x faster                                                   |
| float                   | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                   |
| asyncio_tcp             | 508 ms                                                     | 501 ms: 1.01x faster                                                    |
| 2to3                    | 274 ms                                                     | 270 ms: 1.01x faster                                                    |
| raytrace                | 267 ms                                                     | 263 ms: 1.01x faster                                                    |
| pprint_pformat          | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                  |
| sqlglot_optimize        | 55.5 ms                                                    | 54.8 ms: 1.01x faster                                                   |
| sqlglot_transpile       | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                   |
| regex_compile           | 137 ms                                                     | 135 ms: 1.01x faster                                                    |
| sympy_str               | 282 ms                                                     | 279 ms: 1.01x faster                                                    |
| scimark_monte_carlo     | 69.2 ms                                                    | 68.5 ms: 1.01x faster                                                   |
| json_dumps              | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| deepcopy_memo           | 39.7 us                                                    | 39.3 us: 1.01x faster                                                   |
| meteor_contest          | 110 ms                                                     | 109 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 3.35 us                                                    | 3.32 us: 1.01x faster                                                   |
| sqlglot_parse           | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                   |
| logging_simple          | 5.74 us                                                    | 5.69 us: 1.01x faster                                                   |
| scimark_sor             | 127 ms                                                     | 126 ms: 1.01x faster                                                    |
| sympy_integrate         | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                                   |
| pickle_list             | 5.11 us                                                    | 5.06 us: 1.01x faster                                                   |
| python_startup          | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                   |
| pprint_safe_repr        | 758 ms                                                     | 753 ms: 1.01x faster                                                    |
| sqlglot_normalize       | 110 ms                                                     | 109 ms: 1.01x faster                                                    |
| tornado_http            | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                   |
| telco                   | 8.41 ms                                                    | 8.36 ms: 1.01x faster                                                   |
| sqlite_synth            | 2.99 us                                                    | 2.97 us: 1.01x faster                                                   |
| coverage                | 93.1 ms                                                    | 92.5 ms: 1.01x faster                                                   |
| sympy_sum               | 156 ms                                                     | 155 ms: 1.01x faster                                                    |
| pidigits                | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| sympy_expand            | 473 ms                                                     | 470 ms: 1.01x faster                                                    |
| generators              | 29.6 ms                                                    | 29.5 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.84 sec: 1.00x faster                                                  |
| python_startup_no_site  | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                   |
| genshi_xml              | 51.6 ms                                                    | 52.0 ms: 1.01x slower                                                   |
| json                    | 5.31 ms                                                    | 5.35 ms: 1.01x slower                                                   |
| async_generators        | 442 ms                                                     | 447 ms: 1.01x slower                                                    |
| coroutines              | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                   |
| tomli_loads             | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                                  |
| unpickle_pure_python    | 218 us                                                     | 221 us: 1.01x slower                                                    |
| mako                    | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                   |
| unpickle_list           | 5.34 us                                                    | 5.42 us: 1.01x slower                                                   |
| comprehensions          | 16.6 us                                                    | 16.9 us: 1.02x slower                                                   |
| regex_effbot            | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                   |
| pickle_dict             | 34.8 us                                                    | 35.6 us: 1.02x slower                                                   |
| pickle                  | 11.5 us                                                    | 11.9 us: 1.04x slower                                                   |
| regex_dna               | 221 ms                                                     | 229 ms: 1.04x slower                                                    |
| pycparser               | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                  |
| regex_v8                | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                   |
| Geometric mean          | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (24): async_tree_none, async_tree_memoization_tg, pylint, dask, nbody, html5lib, json_loads, bench_thread_pool, async_tree_cpu_io_mixed_tg, deepcopy, hexiom, deltablue, bench_mp_pool, pickle_pure_python, django_template, xml_etree_iterparse, async_tree_none_tg, typing_runtime_protocols, unpickle, asyncio_websockets, fannkuch, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x