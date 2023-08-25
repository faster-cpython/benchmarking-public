
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 38612a0
- commit date: 2022-06-26
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                  |
| tornado_http   | 96.3 ms                                                | 92.1 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.1 ms: 1.09x faster                                  |
| pidigits       | 198 ms                                                 | 194 ms: 1.02x faster                                   |
| nbody          | 93.1 ms                                                | 94.8 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.61 ms: 1.11x faster                                  |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.04x faster                                  |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                   |
| json_loads           | 26.5 us                                                | 24.5 us: 1.08x faster                                  |
| json_dumps           | 12.6 ms                                                | 12.0 ms: 1.05x faster                                  |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 52.0 ms: 1.04x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.1 us: 1.03x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.02x faster                                   |
| xml_etree_generate   | 76.2 ms                                                | 75.0 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_list          | 4.11 us                                                | 4.15 us: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.26 ms: 1.03x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.10 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.46 ms: 1.07x faster                                  |
| django_template | 32.6 ms                                                | 31.6 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.89 ms: 1.16x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                   |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                  |
| logging_silent          | 101 ns                                                 | 89.6 ns: 1.13x faster                                  |
| pycparser               | 1.18 sec                                               | 1.05 sec: 1.13x faster                                 |
| regex_effbot            | 3.99 ms                                                | 3.61 ms: 1.11x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 62.4 ms: 1.09x faster                                  |
| go                      | 140 ms                                                 | 128 ms: 1.09x faster                                   |
| float                   | 77.2 ms                                                | 71.1 ms: 1.09x faster                                  |
| chaos                   | 69.2 ms                                                | 63.8 ms: 1.08x faster                                  |
| json_loads              | 26.5 us                                                | 24.5 us: 1.08x faster                                  |
| scimark_fft             | 328 ms                                                 | 304 ms: 1.08x faster                                   |
| spectral_norm           | 100 ms                                                 | 92.8 ms: 1.08x faster                                  |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.08x faster                                   |
| hexiom                  | 6.37 ms                                                | 5.94 ms: 1.07x faster                                  |
| mako                    | 10.1 ms                                                | 9.46 ms: 1.07x faster                                  |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                   |
| scimark_lu              | 110 ms                                                 | 104 ms: 1.06x faster                                   |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                   |
| json                    | 4.94 ms                                                | 4.72 ms: 1.05x faster                                  |
| sympy_str               | 290 ms                                                 | 277 ms: 1.05x faster                                   |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                   |
| json_dumps              | 12.6 ms                                                | 12.0 ms: 1.05x faster                                  |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.05x faster                                   |
| tornado_http            | 96.3 ms                                                | 92.1 ms: 1.05x faster                                  |
| logging_format          | 6.68 us                                                | 6.40 us: 1.04x faster                                  |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.04x faster                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                   |
| pickle_pure_python      | 306 us                                                 | 294 us: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| html5lib                | 64.5 ms                                                | 62.0 ms: 1.04x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 52.0 ms: 1.04x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.04x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.1 us: 1.03x faster                                  |
| python_startup          | 8.52 ms                                                | 8.26 ms: 1.03x faster                                  |
| dulwich_log             | 63.7 ms                                                | 61.7 ms: 1.03x faster                                  |
| django_template         | 32.6 ms                                                | 31.6 ms: 1.03x faster                                  |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 155 ms: 1.02x faster                                   |
| pidigits                | 198 ms                                                 | 194 ms: 1.02x faster                                   |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.0 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 745 us: 1.01x faster                                   |
| nqueens                 | 83.4 ms                                                | 82.2 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.7 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| unpack_sequence         | 43.1 ns                                                | 42.8 ns: 1.01x faster                                  |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                  |
| pickle_list             | 4.11 us                                                | 4.15 us: 1.01x slower                                  |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.10 ms: 1.02x slower                                  |
| nbody                   | 93.1 ms                                                | 94.8 ms: 1.02x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.57 us: 1.02x slower                                  |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (4): unpickle, richards, chameleon, unpickle_list
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
