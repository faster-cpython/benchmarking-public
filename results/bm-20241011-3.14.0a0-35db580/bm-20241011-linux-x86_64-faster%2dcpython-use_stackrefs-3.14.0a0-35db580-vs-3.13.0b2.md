# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 35db580
- commit date: 2024-10-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 259 ms: 1.06x faster                                                     |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                   |
| html5lib       | 67.2 ms                                                    | 62.5 ms: 1.08x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 334 ms: 1.13x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.08x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 417 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 578 ms: 1.06x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 886 ms: 1.06x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 560 ms: 1.05x faster                                                     |
| async_tree_io              | 939 ms                                                     | 960 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                     |
| float          | 78.9 ms                                                    | 79.4 ms: 1.01x slower                                                    |
| nbody          | 88.3 ms                                                    | 93.2 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.05x faster                                                     |
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.04x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                    |
| regex_dna      | 221 ms                                                     | 218 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                      | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                     |
| unpickle_list        | 5.34 us                                                    | 5.23 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                     |
| pickle_dict          | 34.8 us                                                    | 34.1 us: 1.02x faster                                                    |
| xml_etree_process    | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 86.6 ms: 1.01x faster                                                    |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                    |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                     |
| pickle               | 11.5 us                                                    | 11.4 us: 1.00x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 315 us: 1.03x slower                                                     |
| json_dumps           | 10.7 ms                                                    | 11.8 ms: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (2): tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                    |
| genshi_xml      | 51.6 ms                                                    | 50.1 ms: 1.03x faster                                                    |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                    |
| mako            | 11.2 ms                                                    | 11.8 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                     |
| deepcopy_memo              | 39.7 us                                                    | 31.2 us: 1.27x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.78 us: 1.21x faster                                                    |
| go                         | 145 ms                                                     | 121 ms: 1.20x faster                                                     |
| async_tree_none            | 378 ms                                                     | 334 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.70 ms: 1.12x faster                                                    |
| coverage                   | 93.1 ms                                                    | 84.7 ms: 1.10x faster                                                    |
| scimark_fft                | 392 ms                                                     | 361 ms: 1.09x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.08x faster                                                     |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                     |
| richards                   | 50.9 ms                                                    | 47.3 ms: 1.08x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 62.5 ms: 1.08x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 417 ms: 1.06x faster                                                     |
| richards_super             | 57.4 ms                                                    | 54.0 ms: 1.06x faster                                                    |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                    |
| 2to3                       | 274 ms                                                     | 259 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 578 ms: 1.06x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 886 ms: 1.06x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.06x faster                                                    |
| genshi_text                | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 483 ms: 1.05x faster                                                     |
| sqlite_synth               | 2.99 us                                                    | 2.84 us: 1.05x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.79 sec: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 560 ms: 1.05x faster                                                     |
| regex_compile              | 137 ms                                                     | 131 ms: 1.05x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                    |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.04x faster                                                    |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.04x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                   |
| genshi_xml                 | 51.6 ms                                                    | 50.1 ms: 1.03x faster                                                    |
| dulwich_log                | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 75.5 ms: 1.03x faster                                                    |
| thrift                     | 823 us                                                     | 802 us: 1.03x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                    |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                     |
| unpickle_list              | 5.34 us                                                    | 5.23 us: 1.02x faster                                                    |
| sympy_str                  | 282 ms                                                     | 276 ms: 1.02x faster                                                     |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                     |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                                    |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                     |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                    |
| sympy_integrate            | 20.5 ms                                                    | 20.2 ms: 1.02x faster                                                    |
| generators                 | 29.6 ms                                                    | 29.2 ms: 1.02x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 60.3 ms: 1.01x faster                                                    |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.01x faster                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 54.9 ms: 1.01x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.40 us: 1.01x faster                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.03 ms: 1.01x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 86.6 ms: 1.01x faster                                                    |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                                     |
| pickle_list                | 5.11 us                                                    | 5.06 us: 1.01x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.63 ms: 1.01x faster                                                    |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.00x faster                                                    |
| raytrace                   | 267 ms                                                     | 267 ms: 1.00x slower                                                     |
| async_generators           | 442 ms                                                     | 444 ms: 1.00x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.32 ms: 1.00x slower                                                    |
| pprint_safe_repr           | 758 ms                                                     | 763 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                   |
| float                      | 78.9 ms                                                    | 79.4 ms: 1.01x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 82.0 ms: 1.01x slower                                                    |
| logging_simple             | 5.74 us                                                    | 5.80 us: 1.01x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                    |
| pyflate                    | 484 ms                                                     | 490 ms: 1.01x slower                                                     |
| chaos                      | 61.3 ms                                                    | 62.1 ms: 1.01x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                    |
| async_tree_io              | 939 ms                                                     | 960 ms: 1.02x slower                                                     |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 858 us: 1.03x slower                                                     |
| comprehensions             | 16.6 us                                                    | 17.1 us: 1.03x slower                                                    |
| pickle_pure_python         | 305 us                                                     | 315 us: 1.03x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                   |
| fannkuch                   | 402 ms                                                     | 418 ms: 1.04x slower                                                     |
| mako                       | 11.2 ms                                                    | 11.8 ms: 1.05x slower                                                    |
| nbody                      | 88.3 ms                                                    | 93.2 ms: 1.06x slower                                                    |
| coroutines                 | 23.2 ms                                                    | 25.3 ms: 1.09x slower                                                    |
| json_dumps                 | 10.7 ms                                                    | 11.8 ms: 1.10x slower                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 56.2 ms: 2.35x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                             |

Benchmark hidden because not significant (7): scimark_monte_carlo, typing_runtime_protocols, sqlglot_parse, sympy_expand, tomli_loads, unpickle, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241011-3.14.0a0-35db580/bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x