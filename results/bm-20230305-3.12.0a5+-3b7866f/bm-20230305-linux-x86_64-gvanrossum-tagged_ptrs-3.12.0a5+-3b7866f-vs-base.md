
# Results vs. base

- fork: gvanrossum
- ref: tagged_ptrs
- machine: linux-x86_64
- commit hash: 3b7866f
- commit date: 2023-03-05
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 255 ms: 1.02x slower                                              |
| chameleon      | 6.50 ms                                                                | 6.64 ms: 1.02x slower                                             |
| docutils       | 2.56 sec                                                               | 2.59 sec: 1.01x slower                                            |
| tornado_http   | 95.1 ms                                                                | 96.0 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 193 ms: 1.02x slower                                              |
| nbody          | 94.5 ms                                                                | 101 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.68 ms                                                                | 3.36 ms: 1.10x faster                                             |
| regex_compile  | 135 ms                                                                 | 138 ms: 1.02x slower                                              |
| regex_v8       | 21.6 ms                                                                | 22.5 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 23.9 us                                                                | 23.7 us: 1.01x faster                                             |
| xml_etree_parse      | 148 ms                                                                 | 149 ms: 1.01x slower                                              |
| xml_etree_process    | 56.4 ms                                                                | 57.4 ms: 1.02x slower                                             |
| json_dumps           | 9.40 ms                                                                | 9.58 ms: 1.02x slower                                             |
| xml_etree_generate   | 81.5 ms                                                                | 83.1 ms: 1.02x slower                                             |
| pickle_pure_python   | 289 us                                                                 | 297 us: 1.03x slower                                              |
| pickle               | 9.88 us                                                                | 10.2 us: 1.03x slower                                             |
| unpickle_pure_python | 201 us                                                                 | 208 us: 1.03x slower                                              |
| unpickle_list        | 4.95 us                                                                | 5.11 us: 1.03x slower                                             |
| unpickle             | 13.2 us                                                                | 13.7 us: 1.03x slower                                             |
| pickle_dict          | 29.9 us                                                                | 31.3 us: 1.05x slower                                             |
| pickle_list          | 3.99 us                                                                | 4.24 us: 1.06x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 9.05 ms                                                                | 9.02 ms: 1.00x faster                                             |
| python_startup_no_site | 6.55 ms                                                                | 6.54 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 33.2 ms                                                                | 34.3 ms: 1.03x slower                                             |
| genshi_text     | 21.2 ms                                                                | 22.0 ms: 1.04x slower                                             |
| genshi_xml      | 47.9 ms                                                                | 49.7 ms: 1.04x slower                                             |
| mako            | 9.91 ms                                                                | 10.5 ms: 1.06x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230303-linux-x86_64-python-cb944d0be869dfb11892-3.12.0a5+-cb944d0 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot            | 3.68 ms                                                                | 3.36 ms: 1.10x faster                                             |
| create_gc_cycles        | 1.49 ms                                                                | 1.47 ms: 1.02x faster                                             |
| json_loads              | 23.9 us                                                                | 23.7 us: 1.01x faster                                             |
| asyncio_tcp             | 507 ms                                                                 | 505 ms: 1.00x faster                                              |
| python_startup          | 9.05 ms                                                                | 9.02 ms: 1.00x faster                                             |
| python_startup_no_site  | 6.55 ms                                                                | 6.54 ms: 1.00x faster                                             |
| sympy_expand            | 464 ms                                                                 | 467 ms: 1.01x slower                                              |
| xml_etree_parse         | 148 ms                                                                 | 149 ms: 1.01x slower                                              |
| async_generators        | 419 ms                                                                 | 423 ms: 1.01x slower                                              |
| sqlite_synth            | 2.60 us                                                                | 2.63 us: 1.01x slower                                             |
| sympy_sum               | 168 ms                                                                 | 169 ms: 1.01x slower                                              |
| tornado_http            | 95.1 ms                                                                | 96.0 ms: 1.01x slower                                             |
| pathlib                 | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                             |
| docutils                | 2.56 sec                                                               | 2.59 sec: 1.01x slower                                            |
| raytrace                | 296 ms                                                                 | 299 ms: 1.01x slower                                              |
| meteor_contest          | 103 ms                                                                 | 105 ms: 1.01x slower                                              |
| logging_format          | 6.39 us                                                                | 6.46 us: 1.01x slower                                             |
| dask                    | 511 ms                                                                 | 517 ms: 1.01x slower                                              |
| generators              | 31.0 ms                                                                | 31.3 ms: 1.01x slower                                             |
| sympy_integrate         | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                             |
| aiohttp                 | 1.01 ms                                                                | 1.02 ms: 1.01x slower                                             |
| sympy_str               | 287 ms                                                                 | 291 ms: 1.01x slower                                              |
| dulwich_log             | 63.4 ms                                                                | 64.3 ms: 1.01x slower                                             |
| thrift                  | 772 us                                                                 | 783 us: 1.01x slower                                              |
| gunicorn                | 1.08 ms                                                                | 1.10 ms: 1.01x slower                                             |
| pidigits                | 190 ms                                                                 | 193 ms: 1.02x slower                                              |
| mypy2                   | 334 ms                                                                 | 340 ms: 1.02x slower                                              |
| 2to3                    | 251 ms                                                                 | 255 ms: 1.02x slower                                              |
| telco                   | 6.48 ms                                                                | 6.59 ms: 1.02x slower                                             |
| xml_etree_process       | 56.4 ms                                                                | 57.4 ms: 1.02x slower                                             |
| bench_thread_pool       | 794 us                                                                 | 808 us: 1.02x slower                                              |
| json_dumps              | 9.40 ms                                                                | 9.58 ms: 1.02x slower                                             |
| xml_etree_generate      | 81.5 ms                                                                | 83.1 ms: 1.02x slower                                             |
| crypto_pyaes            | 74.4 ms                                                                | 75.9 ms: 1.02x slower                                             |
| regex_compile           | 135 ms                                                                 | 138 ms: 1.02x slower                                              |
| chameleon               | 6.50 ms                                                                | 6.64 ms: 1.02x slower                                             |
| coroutines              | 23.5 ms                                                                | 24.0 ms: 1.02x slower                                             |
| logging_simple          | 5.78 us                                                                | 5.92 us: 1.02x slower                                             |
| deltablue               | 3.26 ms                                                                | 3.34 ms: 1.03x slower                                             |
| pprint_pformat          | 1.41 sec                                                               | 1.45 sec: 1.03x slower                                            |
| pickle_pure_python      | 289 us                                                                 | 297 us: 1.03x slower                                              |
| pickle                  | 9.88 us                                                                | 10.2 us: 1.03x slower                                             |
| scimark_lu              | 112 ms                                                                 | 115 ms: 1.03x slower                                              |
| djangocms               | 32.2 us                                                                | 33.1 us: 1.03x slower                                             |
| async_tree_memoization  | 651 ms                                                                 | 670 ms: 1.03x slower                                              |
| pprint_safe_repr        | 689 ms                                                                 | 710 ms: 1.03x slower                                              |
| coverage                | 94.1 ms                                                                | 97.0 ms: 1.03x slower                                             |
| unpickle_pure_python    | 201 us                                                                 | 208 us: 1.03x slower                                              |
| sqlglot_parse           | 1.43 ms                                                                | 1.48 ms: 1.03x slower                                             |
| pycparser               | 1.10 sec                                                               | 1.14 sec: 1.03x slower                                            |
| sqlglot_transpile       | 1.72 ms                                                                | 1.78 ms: 1.03x slower                                             |
| unpickle_list           | 4.95 us                                                                | 5.11 us: 1.03x slower                                             |
| django_template         | 33.2 ms                                                                | 34.3 ms: 1.03x slower                                             |
| unpickle                | 13.2 us                                                                | 13.7 us: 1.03x slower                                             |
| sqlglot_optimize        | 50.9 ms                                                                | 52.6 ms: 1.03x slower                                             |
| deepcopy                | 335 us                                                                 | 346 us: 1.03x slower                                              |
| fannkuch                | 372 ms                                                                 | 385 ms: 1.03x slower                                              |
| pyflate                 | 406 ms                                                                 | 420 ms: 1.04x slower                                              |
| sqlglot_normalize       | 104 ms                                                                 | 108 ms: 1.04x slower                                              |
| genshi_text             | 21.2 ms                                                                | 22.0 ms: 1.04x slower                                             |
| genshi_xml              | 47.9 ms                                                                | 49.7 ms: 1.04x slower                                             |
| nqueens                 | 83.6 ms                                                                | 86.7 ms: 1.04x slower                                             |
| hexiom                  | 6.26 ms                                                                | 6.49 ms: 1.04x slower                                             |
| mdp                     | 2.56 sec                                                               | 2.66 sec: 1.04x slower                                            |
| regex_v8                | 21.6 ms                                                                | 22.5 ms: 1.04x slower                                             |
| comprehensions          | 24.2 us                                                                | 25.2 us: 1.04x slower                                             |
| deepcopy_reduce         | 2.99 us                                                                | 3.12 us: 1.04x slower                                             |
| unpack_sequence         | 42.7 ns                                                                | 44.8 ns: 1.05x slower                                             |
| pickle_dict             | 29.9 us                                                                | 31.3 us: 1.05x slower                                             |
| chaos                   | 67.3 ms                                                                | 70.7 ms: 1.05x slower                                             |
| logging_silent          | 93.8 ns                                                                | 98.7 ns: 1.05x slower                                             |
| scimark_sor             | 109 ms                                                                 | 115 ms: 1.05x slower                                              |
| mako                    | 9.91 ms                                                                | 10.5 ms: 1.06x slower                                             |
| scimark_monte_carlo     | 66.9 ms                                                                | 70.9 ms: 1.06x slower                                             |
| pickle_list             | 3.99 us                                                                | 4.24 us: 1.06x slower                                             |
| gc_traversal            | 3.83 ms                                                                | 4.07 ms: 1.06x slower                                             |
| deepcopy_memo           | 34.7 us                                                                | 36.8 us: 1.06x slower                                             |
| nbody                   | 94.5 ms                                                                | 101 ms: 1.07x slower                                              |
| spectral_norm           | 95.8 ms                                                                | 102 ms: 1.07x slower                                              |
| scimark_fft             | 316 ms                                                                 | 337 ms: 1.07x slower                                              |
| scimark_sparse_mat_mult | 4.46 ms                                                                | 4.86 ms: 1.09x slower                                             |
| Geometric mean          | (ref)                                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (13): bench_mp_pool, richards, go, regex_dna, json, async_tree_cpu_io_mixed, sqlalchemy_declarative, async_tree_io, float, xml_etree_iterparse, async_tree_none, html5lib, sqlalchemy_imperative
