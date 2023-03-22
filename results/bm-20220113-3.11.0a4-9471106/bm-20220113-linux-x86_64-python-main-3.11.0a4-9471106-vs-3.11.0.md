
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9471106
- commit date: 2022-01-13
- overall geometric mean: 1.04x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| chameleon      | 6.38 ms                                                | 7.55 ms: 1.18x slower                                 |
| html5lib       | 64.8 ms                                                | 68.1 ms: 1.05x slower                                 |
| tornado_http   | 96.5 ms                                                | 107 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 197 ms                                                 | 194 ms: 1.02x faster                                  |
| float          | 76.8 ms                                                | 78.0 ms: 1.02x slower                                 |
| nbody          | 90.0 ms                                                | 95.1 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.25 ms: 1.06x faster                                 |
| regex_compile  | 136 ms                                                 | 138 ms: 1.01x slower                                  |
| regex_dna      | 203 ms                                                 | 212 ms: 1.04x slower                                  |
| regex_v8       | 22.2 ms                                                | 24.8 ms: 1.12x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 26.8 us: 1.16x faster                                 |
| json_loads           | 26.1 us                                                | 25.1 us: 1.04x faster                                 |
| xml_etree_parse      | 160 ms                                                 | 155 ms: 1.04x faster                                  |
| pickle               | 9.90 us                                                | 9.95 us: 1.00x slower                                 |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                  |
| unpickle_list        | 4.99 us                                                | 5.20 us: 1.04x slower                                 |
| pickle_list          | 4.14 us                                                | 4.37 us: 1.05x slower                                 |
| xml_etree_generate   | 75.9 ms                                                | 80.2 ms: 1.06x slower                                 |
| xml_etree_process    | 53.7 ms                                                | 56.9 ms: 1.06x slower                                 |
| pickle_pure_python   | 308 us                                                 | 329 us: 1.07x slower                                  |
| unpickle             | 13.3 us                                                | 14.3 us: 1.08x slower                                 |
| unpickle_pure_python | 227 us                                                 | 254 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.07 ms: 1.06x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 5.85 ms: 1.03x faster                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.3 ms                                                | 35.2 ms: 1.09x slower                                 |
| mako            | 9.83 ms                                                | 11.5 ms: 1.17x slower                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 31.2 us                                                | 26.8 us: 1.16x faster                                 |
| regex_effbot            | 3.46 ms                                                | 3.25 ms: 1.06x faster                                 |
| python_startup          | 8.58 ms                                                | 8.07 ms: 1.06x faster                                 |
| json_loads              | 26.1 us                                                | 25.1 us: 1.04x faster                                 |
| xml_etree_parse         | 160 ms                                                 | 155 ms: 1.04x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 5.85 ms: 1.03x faster                                 |
| json                    | 4.87 ms                                                | 4.74 ms: 1.03x faster                                 |
| pycparser               | 1.19 sec                                               | 1.17 sec: 1.02x faster                                |
| pidigits                | 197 ms                                                 | 194 ms: 1.02x faster                                  |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                  |
| logging_simple          | 6.02 us                                                | 5.95 us: 1.01x faster                                 |
| logging_format          | 6.48 us                                                | 6.51 us: 1.00x slower                                 |
| pickle                  | 9.90 us                                                | 9.95 us: 1.00x slower                                 |
| spectral_norm           | 98.1 ms                                                | 99.0 ms: 1.01x slower                                 |
| scimark_fft             | 325 ms                                                 | 330 ms: 1.01x slower                                  |
| regex_compile           | 136 ms                                                 | 138 ms: 1.01x slower                                  |
| float                   | 76.8 ms                                                | 78.0 ms: 1.02x slower                                 |
| 2to3                    | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| fannkuch                | 384 ms                                                 | 392 ms: 1.02x slower                                  |
| sympy_integrate         | 21.0 ms                                                | 21.4 ms: 1.02x slower                                 |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.69 ms: 1.02x slower                                 |
| sympy_sum               | 166 ms                                                 | 170 ms: 1.02x slower                                  |
| dulwich_log             | 64.0 ms                                                | 65.8 ms: 1.03x slower                                 |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                  |
| sympy_str               | 291 ms                                                 | 302 ms: 1.04x slower                                  |
| telco                   | 6.43 ms                                                | 6.69 ms: 1.04x slower                                 |
| regex_dna               | 203 ms                                                 | 212 ms: 1.04x slower                                  |
| unpickle_list           | 4.99 us                                                | 5.20 us: 1.04x slower                                 |
| hexiom                  | 6.34 ms                                                | 6.63 ms: 1.05x slower                                 |
| html5lib                | 64.8 ms                                                | 68.1 ms: 1.05x slower                                 |
| pickle_list             | 4.14 us                                                | 4.37 us: 1.05x slower                                 |
| scimark_lu              | 108 ms                                                 | 114 ms: 1.05x slower                                  |
| go                      | 140 ms                                                 | 148 ms: 1.06x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.2 ms: 1.06x slower                                 |
| nbody                   | 90.0 ms                                                | 95.1 ms: 1.06x slower                                 |
| pathlib                 | 18.1 ms                                                | 19.1 ms: 1.06x slower                                 |
| chaos                   | 68.7 ms                                                | 72.7 ms: 1.06x slower                                 |
| pyflate                 | 419 ms                                                 | 444 ms: 1.06x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 56.9 ms: 1.06x slower                                 |
| sympy_expand            | 475 ms                                                 | 506 ms: 1.06x slower                                  |
| pickle_pure_python      | 308 us                                                 | 329 us: 1.07x slower                                  |
| thrift                  | 760 us                                                 | 812 us: 1.07x slower                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 72.7 ms: 1.07x slower                                 |
| unpickle                | 13.3 us                                                | 14.3 us: 1.08x slower                                 |
| scimark_sor             | 115 ms                                                 | 124 ms: 1.08x slower                                  |
| django_template         | 32.3 ms                                                | 35.2 ms: 1.09x slower                                 |
| raytrace                | 291 ms                                                 | 320 ms: 1.10x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.73 us: 1.10x slower                                 |
| tornado_http            | 96.5 ms                                                | 107 ms: 1.11x slower                                  |
| crypto_pyaes            | 75.7 ms                                                | 83.8 ms: 1.11x slower                                 |
| regex_v8                | 22.2 ms                                                | 24.8 ms: 1.12x slower                                 |
| richards                | 46.1 ms                                                | 51.5 ms: 1.12x slower                                 |
| unpickle_pure_python    | 227 us                                                 | 254 us: 1.12x slower                                  |
| deltablue               | 3.66 ms                                                | 4.16 ms: 1.14x slower                                 |
| logging_silent          | 98.0 ns                                                | 113 ns: 1.16x slower                                  |
| mako                    | 9.83 ms                                                | 11.5 ms: 1.17x slower                                 |
| chameleon               | 6.38 ms                                                | 7.55 ms: 1.18x slower                                 |
| Geometric mean          | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (3): json_dumps, nqueens, unpack_sequence
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
