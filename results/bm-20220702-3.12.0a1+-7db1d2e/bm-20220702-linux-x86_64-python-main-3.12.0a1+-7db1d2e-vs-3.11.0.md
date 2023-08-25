
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7db1d2e
- commit date: 2022-07-02
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| chameleon      | 6.47 ms                                                | 6.39 ms: 1.01x faster                                  |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.4 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 69.9 ms: 1.10x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nbody          | 93.1 ms                                                | 89.9 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.49 ms: 1.15x faster                                  |
| regex_compile  | 138 ms                                                 | 125 ms: 1.11x faster                                   |
| regex_dna      | 204 ms                                                 | 197 ms: 1.04x faster                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                   |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                   |
| json_dumps           | 12.6 ms                                                | 11.9 ms: 1.05x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 52.0 ms: 1.04x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 75.0 ms: 1.02x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                   |
| unpickle_list        | 4.91 us                                                | 4.93 us: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| pickle_list          | 4.11 us                                                | 4.28 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.22 ms: 1.04x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.07 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.55 ms: 1.06x faster                                  |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                   |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.49 ms: 1.15x faster                                  |
| regex_compile           | 138 ms                                                 | 125 ms: 1.11x faster                                   |
| float                   | 77.2 ms                                                | 69.9 ms: 1.10x faster                                  |
| logging_silent          | 101 ns                                                 | 91.7 ns: 1.10x faster                                  |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                 |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                  |
| hexiom                  | 6.37 ms                                                | 5.88 ms: 1.08x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 62.8 ms: 1.08x faster                                  |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                   |
| pyflate                 | 418 ms                                                 | 389 ms: 1.08x faster                                   |
| go                      | 140 ms                                                 | 130 ms: 1.07x faster                                   |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.21 ms: 1.07x faster                                  |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.06x faster                                   |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                   |
| spectral_norm           | 100 ms                                                 | 94.3 ms: 1.06x faster                                  |
| chaos                   | 69.2 ms                                                | 65.2 ms: 1.06x faster                                  |
| mako                    | 10.1 ms                                                | 9.55 ms: 1.06x faster                                  |
| sympy_expand            | 475 ms                                                 | 450 ms: 1.06x faster                                   |
| json_dumps              | 12.6 ms                                                | 11.9 ms: 1.05x faster                                  |
| tornado_http            | 96.3 ms                                                | 91.4 ms: 1.05x faster                                  |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                  |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                   |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.05x faster                                   |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                  |
| sympy_str               | 290 ms                                                 | 276 ms: 1.05x faster                                   |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.05x faster                                   |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| html5lib                | 64.5 ms                                                | 62.0 ms: 1.04x faster                                  |
| dulwich_log             | 63.7 ms                                                | 61.2 ms: 1.04x faster                                  |
| fannkuch                | 388 ms                                                 | 373 ms: 1.04x faster                                   |
| regex_dna               | 204 ms                                                 | 197 ms: 1.04x faster                                   |
| python_startup          | 8.52 ms                                                | 8.22 ms: 1.04x faster                                  |
| nbody                   | 93.1 ms                                                | 89.9 ms: 1.04x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 52.0 ms: 1.04x faster                                  |
| nqueens                 | 83.4 ms                                                | 81.0 ms: 1.03x faster                                  |
| richards                | 45.7 ms                                                | 44.6 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.3 ms: 1.02x faster                                  |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 744 us: 1.02x faster                                   |
| xml_etree_generate      | 76.2 ms                                                | 75.0 ms: 1.02x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.01x faster                                   |
| chameleon               | 6.47 ms                                                | 6.39 ms: 1.01x faster                                  |
| unpickle_list           | 4.91 us                                                | 4.93 us: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.07 ms: 1.01x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                  |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| pickle_list             | 4.11 us                                                | 4.28 us: 1.04x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 45.5 ns: 1.05x slower                                  |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (3): unpickle, regex_v8, telco
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
