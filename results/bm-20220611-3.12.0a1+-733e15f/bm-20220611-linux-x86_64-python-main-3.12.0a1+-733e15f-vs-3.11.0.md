
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 733e15f
- commit date: 2022-06-11
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| chameleon      | 6.38 ms                                                | 6.40 ms: 1.00x slower                                  |
| html5lib       | 64.8 ms                                                | 63.4 ms: 1.02x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.3 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.0 ms: 1.08x faster                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x faster                                   |
| nbody          | 90.0 ms                                                | 91.3 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.01 ms: 1.15x faster                                  |
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.05x faster                                  |
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                   |
| regex_dna      | 203 ms                                                 | 198 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 227 us                                                 | 212 us: 1.07x faster                                   |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                   |
| json_loads           | 26.1 us                                                | 25.1 us: 1.04x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.1 ms: 1.03x faster                                  |
| json_dumps           | 12.4 ms                                                | 12.0 ms: 1.03x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.89 us: 1.02x faster                                  |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                  |
| pickle_list          | 4.14 us                                                | 4.11 us: 1.01x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 75.4 ms: 1.01x faster                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| unpickle             | 13.3 us                                                | 14.1 us: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.26 ms: 1.04x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.11 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 32.3 ms                                                | 31.2 ms: 1.04x faster                                  |
| mako            | 9.83 ms                                                | 9.74 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot            | 3.46 ms                                                | 3.01 ms: 1.15x faster                                  |
| pycparser               | 1.19 sec                                               | 1.07 sec: 1.11x faster                                 |
| float                   | 76.8 ms                                                | 71.0 ms: 1.08x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 212 us: 1.07x faster                                   |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                   |
| scimark_lu              | 108 ms                                                 | 102 ms: 1.06x faster                                   |
| richards                | 46.1 ms                                                | 43.6 ms: 1.06x faster                                  |
| tornado_http            | 96.5 ms                                                | 91.3 ms: 1.06x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.36 ms: 1.05x faster                                  |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                   |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.05x faster                                  |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.04x faster                                   |
| deltablue               | 3.66 ms                                                | 3.51 ms: 1.04x faster                                  |
| json_loads              | 26.1 us                                                | 25.1 us: 1.04x faster                                  |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| python_startup          | 8.58 ms                                                | 8.26 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| django_template         | 32.3 ms                                                | 31.2 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| scimark_fft             | 325 ms                                                 | 315 ms: 1.03x faster                                   |
| dulwich_log             | 64.0 ms                                                | 61.9 ms: 1.03x faster                                  |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                   |
| logging_simple          | 6.02 us                                                | 5.84 us: 1.03x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 52.1 ms: 1.03x faster                                  |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                   |
| spectral_norm           | 98.1 ms                                                | 95.3 ms: 1.03x faster                                  |
| json_dumps              | 12.4 ms                                                | 12.0 ms: 1.03x faster                                  |
| regex_dna               | 203 ms                                                 | 198 ms: 1.03x faster                                   |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.03x faster                                   |
| hexiom                  | 6.34 ms                                                | 6.17 ms: 1.03x faster                                  |
| thrift                  | 760 us                                                 | 741 us: 1.02x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 74.0 ms: 1.02x faster                                  |
| html5lib                | 64.8 ms                                                | 63.4 ms: 1.02x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 43.6 ns: 1.02x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.89 us: 1.02x faster                                  |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                  |
| json                    | 4.87 ms                                                | 4.78 ms: 1.02x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 66.7 ms: 1.02x faster                                  |
| logging_format          | 6.48 us                                                | 6.36 us: 1.02x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                  |
| chaos                   | 68.7 ms                                                | 68.0 ms: 1.01x faster                                  |
| mako                    | 9.83 ms                                                | 9.74 ms: 1.01x faster                                  |
| pickle_list             | 4.14 us                                                | 4.11 us: 1.01x faster                                  |
| fannkuch                | 384 ms                                                 | 382 ms: 1.01x faster                                   |
| xml_etree_generate      | 75.9 ms                                                | 75.4 ms: 1.01x faster                                  |
| nqueens                 | 83.8 ms                                                | 83.4 ms: 1.00x faster                                  |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x faster                                   |
| chameleon               | 6.38 ms                                                | 6.40 ms: 1.00x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.50 us: 1.01x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.11 ms: 1.01x slower                                  |
| logging_silent          | 98.0 ns                                                | 99.2 ns: 1.01x slower                                  |
| nbody                   | 90.0 ms                                                | 91.3 ms: 1.01x slower                                  |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| unpickle                | 13.3 us                                                | 14.1 us: 1.07x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, telco
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
