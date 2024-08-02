# Results vs. 3.13.0b2

- fork: nohlson
- ref: enable_fcf_protectio
- machine: linux-x86_64
- commit hash: 34aead4
- commit date: 2024-06-25
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 265 ms: 1.03x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                 |
| html5lib       | 67.2 ms                                                    | 67.6 ms: 1.01x slower                                                  |
| tornado_http   | 94.6 ms                                                    | 90.9 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 363 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 324 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 984 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (4): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                  |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                  |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                                   |
| regex_v8       | 25.1 ms                                                    | 26.9 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                      | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.02x faster                                                   |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.31 us: 1.01x faster                                                  |
| pickle_list          | 5.11 us                                                    | 5.12 us: 1.00x slower                                                  |
| pickle               | 11.5 us                                                    | 11.5 us: 1.00x slower                                                  |
| pickle_dict          | 34.8 us                                                    | 35.3 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (3): pickle_pure_python, tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 6.94 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                  |
| mako           | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 29.5 us: 1.35x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.23x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                   |
| richards_super             | 57.4 ms                                                    | 53.6 ms: 1.07x faster                                                  |
| richards                   | 50.9 ms                                                    | 47.6 ms: 1.07x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 477 ms: 1.07x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                                  |
| scimark_fft                | 392 ms                                                     | 369 ms: 1.06x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 791 us: 1.05x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.48 us: 1.05x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.04 ms: 1.05x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                 |
| async_tree_none            | 378 ms                                                     | 363 ms: 1.04x faster                                                   |
| dulwich_log                | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 74.4 ms: 1.04x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 90.9 ms: 1.04x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                                  |
| thrift                     | 823 us                                                     | 793 us: 1.04x faster                                                   |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 324 ms: 1.04x faster                                                   |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                  |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.04x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 22.4 ms: 1.04x faster                                                  |
| dask                       | 369 ms                                                     | 357 ms: 1.04x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.03x faster                                                 |
| 2to3                       | 274 ms                                                     | 265 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.89 us: 1.03x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 78.8 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 735 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                                   |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| async_generators           | 442 ms                                                     | 430 ms: 1.03x faster                                                   |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 54.1 ms: 1.03x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 6.94 ms: 1.02x faster                                                  |
| generators                 | 29.6 ms                                                    | 29.0 ms: 1.02x faster                                                  |
| float                      | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                  |
| sympy_str                  | 282 ms                                                     | 276 ms: 1.02x faster                                                   |
| fannkuch                   | 402 ms                                                     | 393 ms: 1.02x faster                                                   |
| telco                      | 8.41 ms                                                    | 8.24 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.92 sec: 1.02x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.17 ms: 1.02x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                   |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                   |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                   |
| genshi_text                | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.02x faster                                                   |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                  |
| sympy_expand               | 473 ms                                                     | 467 ms: 1.01x faster                                                   |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                   |
| pyflate                    | 484 ms                                                     | 480 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                   |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.31 us: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                  |
| pickle_list                | 5.11 us                                                    | 5.12 us: 1.00x slower                                                  |
| pickle                     | 11.5 us                                                    | 11.5 us: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| html5lib                   | 67.2 ms                                                    | 67.6 ms: 1.01x slower                                                  |
| pickle_dict                | 34.8 us                                                    | 35.3 us: 1.02x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                  |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.03x slower                                                   |
| regex_dna                  | 221 ms                                                     | 232 ms: 1.05x slower                                                   |
| async_tree_io_tg           | 936 ms                                                     | 984 ms: 1.05x slower                                                   |
| regex_v8                   | 25.1 ms                                                    | 26.9 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (15): pylint, async_tree_io, coverage, pickle_pure_python, scimark_monte_carlo, django_template, typing_runtime_protocols, async_tree_cpu_io_mixed, nbody, genshi_xml, tomli_loads, json, unpickle, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x