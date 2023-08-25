
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c20186c
- commit date: 2022-07-17
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.28 ms: 1.03x faster                                  |
| html5lib       | 64.5 ms                                                | 62.8 ms: 1.03x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.3 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                  |
| nbody          | 93.1 ms                                                | 88.8 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                  |
| regex_compile  | 138 ms                                                 | 127 ms: 1.08x faster                                   |
| regex_v8       | 22.0 ms                                                | 20.9 ms: 1.05x faster                                  |
| regex_dna      | 204 ms                                                 | 197 ms: 1.04x faster                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                   |
| json_dumps           | 12.6 ms                                                | 11.9 ms: 1.06x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 52.2 ms: 1.03x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 75.2 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| pickle               | 10.1 us                                                | 10.3 us: 1.03x slower                                  |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.17 ms: 1.04x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.02 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.33 ms: 1.08x faster                                  |
| django_template | 32.6 ms                                                | 32.1 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.47 ms: 1.15x faster                                  |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                   |
| pycparser               | 1.18 sec                                               | 1.05 sec: 1.12x faster                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.04 ms: 1.11x faster                                  |
| logging_silent          | 101 ns                                                 | 91.9 ns: 1.10x faster                                  |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| regex_compile           | 138 ms                                                 | 127 ms: 1.08x faster                                   |
| mako                    | 10.1 ms                                                | 9.33 ms: 1.08x faster                                  |
| logging_simple          | 6.03 us                                                | 5.61 us: 1.08x faster                                  |
| logging_format          | 6.68 us                                                | 6.22 us: 1.07x faster                                  |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                  |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                  |
| spectral_norm           | 100 ms                                                 | 93.4 ms: 1.07x faster                                  |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                   |
| json_dumps              | 12.6 ms                                                | 11.9 ms: 1.06x faster                                  |
| nqueens                 | 83.4 ms                                                | 78.8 ms: 1.06x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                   |
| tornado_http            | 96.3 ms                                                | 91.3 ms: 1.05x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.05 ms: 1.05x faster                                  |
| regex_v8                | 22.0 ms                                                | 20.9 ms: 1.05x faster                                  |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                   |
| nbody                   | 93.1 ms                                                | 88.8 ms: 1.05x faster                                  |
| scimark_fft             | 328 ms                                                 | 313 ms: 1.05x faster                                   |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.05x faster                                   |
| dulwich_log             | 63.7 ms                                                | 60.8 ms: 1.05x faster                                  |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.05x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 65.1 ms: 1.05x faster                                  |
| sympy_str               | 290 ms                                                 | 278 ms: 1.04x faster                                   |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| python_startup          | 8.52 ms                                                | 8.17 ms: 1.04x faster                                  |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.04x faster                                   |
| pyflate                 | 418 ms                                                 | 401 ms: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| fannkuch                | 388 ms                                                 | 373 ms: 1.04x faster                                   |
| regex_dna               | 204 ms                                                 | 197 ms: 1.04x faster                                   |
| xml_etree_process       | 53.9 ms                                                | 52.2 ms: 1.03x faster                                  |
| chameleon               | 6.47 ms                                                | 6.28 ms: 1.03x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| html5lib                | 64.5 ms                                                | 62.8 ms: 1.03x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 72.9 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 739 us: 1.02x faster                                   |
| richards                | 45.7 ms                                                | 44.7 ms: 1.02x faster                                  |
| django_template         | 32.6 ms                                                | 32.1 ms: 1.02x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.2 ms: 1.01x faster                                  |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.02 ms: 1.00x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| pickle                  | 10.1 us                                                | 10.3 us: 1.03x slower                                  |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.08 us: 1.03x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (4): unpickle, scimark_sor, unpack_sequence, xml_etree_parse
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
