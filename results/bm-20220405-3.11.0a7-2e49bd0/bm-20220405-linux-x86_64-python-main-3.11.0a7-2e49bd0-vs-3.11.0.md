
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.02x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| chameleon      | 6.38 ms                                                | 6.87 ms: 1.08x slower                                 |
| tornado_http   | 96.5 ms                                                | 95.4 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 76.8 ms                                                | 74.4 ms: 1.03x faster                                 |
| nbody          | 90.0 ms                                                | 95.2 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.34 ms: 1.04x faster                                 |
| regex_compile  | 136 ms                                                 | 137 ms: 1.01x slower                                  |
| regex_dna      | 203 ms                                                 | 231 ms: 1.14x slower                                  |
| regex_v8       | 22.2 ms                                                | 25.9 ms: 1.16x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 27.6 us: 1.13x faster                                 |
| pickle               | 9.90 us                                                | 9.55 us: 1.04x faster                                 |
| xml_etree_parse      | 160 ms                                                 | 157 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 104 ms: 1.00x faster                                  |
| pickle_pure_python   | 308 us                                                 | 311 us: 1.01x slower                                  |
| json_dumps           | 12.4 ms                                                | 12.5 ms: 1.01x slower                                 |
| unpickle_pure_python | 227 us                                                 | 231 us: 1.02x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 55.2 ms: 1.03x slower                                 |
| xml_etree_generate   | 75.9 ms                                                | 78.5 ms: 1.03x slower                                 |
| unpickle             | 13.3 us                                                | 14.1 us: 1.06x slower                                 |
| json_loads           | 26.1 us                                                | 28.1 us: 1.08x slower                                 |
| pickle_list          | 4.14 us                                                | 4.57 us: 1.10x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.07 ms: 1.06x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 5.98 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.83 ms                                                | 10.2 ms: 1.03x slower                                 |
| django_template | 32.3 ms                                                | 34.3 ms: 1.06x slower                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 31.2 us                                                | 27.6 us: 1.13x faster                                 |
| python_startup          | 8.58 ms                                                | 8.07 ms: 1.06x faster                                 |
| logging_simple          | 6.02 us                                                | 5.80 us: 1.04x faster                                 |
| pickle                  | 9.90 us                                                | 9.55 us: 1.04x faster                                 |
| regex_effbot            | 3.46 ms                                                | 3.34 ms: 1.04x faster                                 |
| sympy_sum               | 166 ms                                                 | 160 ms: 1.04x faster                                  |
| float                   | 76.8 ms                                                | 74.4 ms: 1.03x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                 |
| xml_etree_parse         | 160 ms                                                 | 157 ms: 1.02x faster                                  |
| logging_format          | 6.48 us                                                | 6.35 us: 1.02x faster                                 |
| sympy_str               | 291 ms                                                 | 287 ms: 1.01x faster                                  |
| tornado_http            | 96.5 ms                                                | 95.4 ms: 1.01x faster                                 |
| python_startup_no_site  | 6.04 ms                                                | 5.98 ms: 1.01x faster                                 |
| xml_etree_iterparse     | 104 ms                                                 | 104 ms: 1.00x faster                                  |
| dulwich_log             | 64.0 ms                                                | 63.8 ms: 1.00x faster                                 |
| regex_compile           | 136 ms                                                 | 137 ms: 1.01x slower                                  |
| pickle_pure_python      | 308 us                                                 | 311 us: 1.01x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 44.9 ns: 1.01x slower                                 |
| json_dumps              | 12.4 ms                                                | 12.5 ms: 1.01x slower                                 |
| sqlite_synth            | 2.48 us                                                | 2.51 us: 1.01x slower                                 |
| deltablue               | 3.66 ms                                                | 3.70 ms: 1.01x slower                                 |
| go                      | 140 ms                                                 | 143 ms: 1.02x slower                                  |
| unpickle_pure_python    | 227 us                                                 | 231 us: 1.02x slower                                  |
| nqueens                 | 83.8 ms                                                | 85.2 ms: 1.02x slower                                 |
| 2to3                    | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| meteor_contest          | 104 ms                                                 | 107 ms: 1.02x slower                                  |
| pathlib                 | 18.1 ms                                                | 18.5 ms: 1.02x slower                                 |
| chaos                   | 68.7 ms                                                | 70.2 ms: 1.02x slower                                 |
| telco                   | 6.43 ms                                                | 6.59 ms: 1.03x slower                                 |
| scimark_fft             | 325 ms                                                 | 335 ms: 1.03x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 55.2 ms: 1.03x slower                                 |
| richards                | 46.1 ms                                                | 47.5 ms: 1.03x slower                                 |
| xml_etree_generate      | 75.9 ms                                                | 78.5 ms: 1.03x slower                                 |
| mako                    | 9.83 ms                                                | 10.2 ms: 1.03x slower                                 |
| json                    | 4.87 ms                                                | 5.07 ms: 1.04x slower                                 |
| scimark_monte_carlo     | 68.0 ms                                                | 70.8 ms: 1.04x slower                                 |
| fannkuch                | 384 ms                                                 | 401 ms: 1.04x slower                                  |
| pycparser               | 1.19 sec                                               | 1.24 sec: 1.04x slower                                |
| pyflate                 | 419 ms                                                 | 438 ms: 1.05x slower                                  |
| raytrace                | 291 ms                                                 | 306 ms: 1.05x slower                                  |
| nbody                   | 90.0 ms                                                | 95.2 ms: 1.06x slower                                 |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.85 ms: 1.06x slower                                 |
| logging_silent          | 98.0 ns                                                | 104 ns: 1.06x slower                                  |
| django_template         | 32.3 ms                                                | 34.3 ms: 1.06x slower                                 |
| unpickle                | 13.3 us                                                | 14.1 us: 1.06x slower                                 |
| spectral_norm           | 98.1 ms                                                | 105 ms: 1.07x slower                                  |
| scimark_sor             | 115 ms                                                 | 123 ms: 1.07x slower                                  |
| chameleon               | 6.38 ms                                                | 6.87 ms: 1.08x slower                                 |
| json_loads              | 26.1 us                                                | 28.1 us: 1.08x slower                                 |
| hexiom                  | 6.34 ms                                                | 6.84 ms: 1.08x slower                                 |
| crypto_pyaes            | 75.7 ms                                                | 82.7 ms: 1.09x slower                                 |
| pickle_list             | 4.14 us                                                | 4.57 us: 1.10x slower                                 |
| regex_dna               | 203 ms                                                 | 231 ms: 1.14x slower                                  |
| regex_v8                | 22.2 ms                                                | 25.9 ms: 1.16x slower                                 |
| Geometric mean          | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (6): unpickle_list, pidigits, sympy_expand, thrift, scimark_lu, html5lib
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
