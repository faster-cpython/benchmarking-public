# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 4711506
- commit date: 2024-09-19
- overall geometric mean: 1.04x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                |
| html5lib       | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 95.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 319 ms: 1.19x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                  |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 876 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                 |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                  |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.9 ms: 1.12x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 54.6 ms: 1.12x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 98.0 ms: 1.10x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.16 us: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| pickle_dict          | 34.8 us                                                    | 35.2 us: 1.01x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.37 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.97 ms: 1.13x faster                                                 |
| django_template | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                 |
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                                  |
| richards                   | 50.9 ms                                                    | 39.9 ms: 1.28x faster                                                 |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                 |
| richards_super             | 57.4 ms                                                    | 45.6 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.29 ms: 1.23x faster                                                 |
| async_tree_none            | 378 ms                                                     | 319 ms: 1.19x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 67.2 ms: 1.15x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                  |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.97 ms: 1.13x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.47 sec: 1.12x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 77.9 ms: 1.12x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 54.6 ms: 1.12x faster                                                 |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                                 |
| coverage                   | 93.1 ms                                                    | 84.5 ms: 1.10x faster                                                 |
| nbody                      | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                 |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 98.0 ms: 1.10x faster                                                 |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                                  |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                  |
| sqlite_synth               | 2.99 us                                                    | 2.76 us: 1.08x faster                                                 |
| pyflate                    | 484 ms                                                     | 451 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                  |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 876 ms: 1.07x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.94 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.83 ms: 1.04x faster                                                 |
| thrift                     | 823 us                                                     | 794 us: 1.04x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                 |
| unpickle_list              | 5.34 us                                                    | 5.16 us: 1.03x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.70 sec: 1.03x faster                                                |
| json                       | 5.31 ms                                                    | 5.14 ms: 1.03x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 160 us: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.65 us: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                 |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 838 us: 1.00x slower                                                  |
| tornado_http               | 94.6 ms                                                    | 95.1 ms: 1.01x slower                                                 |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                  |
| pickle_dict                | 34.8 us                                                    | 35.2 us: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                 |
| django_template            | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                 |
| async_generators           | 442 ms                                                     | 451 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                 |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 57.9 ms: 1.04x slower                                                 |
| raytrace                   | 267 ms                                                     | 280 ms: 1.05x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                |
| pickle_list                | 5.11 us                                                    | 5.37 us: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 504 ms: 1.07x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 87.9 ms: 1.08x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.98 ms: 1.11x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                 |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                 |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (6): chaos, pickle_pure_python, regex_v8, pprint_safe_repr, pprint_pformat, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240919-3.14.0a0-4711506-JIT/bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506.json: unpack_sequence

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x