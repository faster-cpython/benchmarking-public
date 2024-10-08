# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.04x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                     |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                   |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 93.3 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                     |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                    |
| nbody          | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                    |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                     |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                    |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                      | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 81.3 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 100 ms: 1.07x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                    |
| django_template | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 58.4 ms: 1.13x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.3 us: 1.40x faster                                                    |
| deepcopy                   | 367 us                                                     | 273 us: 1.34x faster                                                     |
| richards                   | 50.9 ms                                                    | 40.4 ms: 1.26x faster                                                    |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                    |
| richards_super             | 57.4 ms                                                    | 46.9 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.81 us: 1.19x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 66.3 ms: 1.17x faster                                                    |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                     |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.8 ms: 1.12x faster                                                    |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                     |
| nbody                      | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                    |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                     |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.10x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 81.3 ms: 1.07x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.84 ms: 1.07x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 707 ms: 1.07x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 100 ms: 1.07x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 874 ms: 1.07x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                    |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                    |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                    |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                     |
| generators                 | 29.6 ms                                                    | 28.8 ms: 1.03x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                     |
| thrift                     | 823 us                                                     | 800 us: 1.03x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                     |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                    |
| tornado_http               | 94.6 ms                                                    | 93.3 ms: 1.02x faster                                                    |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 826 us: 1.01x faster                                                     |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                     |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 56.2 ms: 1.01x slower                                                    |
| raytrace                   | 267 ms                                                     | 270 ms: 1.01x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                   |
| django_template            | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                    |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                                     |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                     |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                   |
| go                         | 145 ms                                                     | 149 ms: 1.03x slower                                                     |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                                    |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.59 ms: 1.05x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 128 ms: 1.06x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.0 ms: 1.06x slower                                                    |
| sympy_expand               | 473 ms                                                     | 501 ms: 1.06x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                    |
| pylint                     | 317 ms                                                     | 351 ms: 1.11x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 3.65 ms: 1.12x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 58.4 ms: 1.13x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                             |

Benchmark hidden because not significant (3): dask, coverage, coroutines
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x