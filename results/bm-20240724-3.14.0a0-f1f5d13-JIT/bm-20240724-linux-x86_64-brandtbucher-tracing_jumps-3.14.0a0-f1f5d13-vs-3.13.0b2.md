# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: f1f5d13
- commit date: 2024-07-24
- overall geometric mean: 1.04x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                 |
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                               |
| html5lib       | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                |
| tornado_http   | 94.6 ms                                                    | 93.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                      | 1.00x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 402 ms: 1.15x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.08x faster                                                 |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                |
| nbody          | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.08x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                |
| regex_dna      | 221 ms                                                     | 237 ms: 1.07x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.97 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                      | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 79.3 ms: 1.10x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                               |
| xml_etree_process    | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                |
| pickle_pure_python   | 305 us                                                     | 294 us: 1.04x faster                                                 |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.03x faster                                                |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.68 ms: 1.16x faster                                                |
| genshi_text     | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 53.2 ms: 1.03x slower                                                |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.6 us: 1.39x faster                                                |
| deepcopy                   | 367 us                                                     | 273 us: 1.34x faster                                                 |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                 |
| richards                   | 50.9 ms                                                    | 40.5 ms: 1.26x faster                                                |
| richards_super             | 57.4 ms                                                    | 46.8 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                                |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.68 ms: 1.16x faster                                                |
| async_tree_memoization     | 463 ms                                                     | 402 ms: 1.15x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.1 ms: 1.15x faster                                                |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                 |
| pyflate                    | 484 ms                                                     | 424 ms: 1.14x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                 |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 529 ms: 1.11x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 79.3 ms: 1.10x faster                                                |
| nbody                      | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.62 ms: 1.10x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                               |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                               |
| xml_etree_process          | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                |
| telco                      | 8.41 ms                                                    | 7.84 ms: 1.07x faster                                                |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                 |
| async_tree_io              | 939 ms                                                     | 899 ms: 1.04x faster                                                 |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                |
| thrift                     | 823 us                                                     | 790 us: 1.04x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 294 us: 1.04x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 734 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                               |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                |
| comprehensions             | 16.6 us                                                    | 16.1 us: 1.03x faster                                                |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.03x faster                                                |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                               |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                 |
| bench_thread_pool          | 834 us                                                     | 818 us: 1.02x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.64 us: 1.02x faster                                                |
| coverage                   | 93.1 ms                                                    | 91.5 ms: 1.02x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 93.7 ms: 1.01x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.63 ms: 1.00x faster                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 55.8 ms: 1.00x slower                                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                 |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                               |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 83.6 ms: 1.03x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 53.2 ms: 1.03x slower                                                |
| dulwich_log                | 67.2 ms                                                    | 69.9 ms: 1.04x slower                                                |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                |
| regex_v8                   | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                                |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                 |
| sympy_expand               | 473 ms                                                     | 504 ms: 1.07x slower                                                 |
| regex_dna                  | 221 ms                                                     | 237 ms: 1.07x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.74 ms: 1.07x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.97 ms: 1.08x slower                                                |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                |
| deltablue                  | 3.25 ms                                                    | 3.56 ms: 1.10x slower                                                |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                |
| pylint                     | 317 ms                                                     | 354 ms: 1.12x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                         |

Benchmark hidden because not significant (2): raytrace, pycparser
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x