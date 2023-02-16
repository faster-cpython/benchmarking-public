
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 264b3dd
- commit date: 2022-07-10
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.30 ms: 1.01x faster                                  |
| html5lib       | 64.8 ms                                                | 62.6 ms: 1.04x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.3 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.4 ms: 1.06x faster                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 126 ms: 1.08x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.1 ms: 1.01x faster                                  |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.54 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                   |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                   |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| json_dumps           | 12.4 ms                                                | 11.8 ms: 1.05x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 156 ms: 1.03x faster                                   |
| xml_etree_process    | 53.7 ms                                                | 53.3 ms: 1.01x faster                                  |
| pickle_list          | 4.14 us                                                | 4.12 us: 1.01x faster                                  |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                  |
| pickle_dict          | 31.2 us                                                | 31.6 us: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.16 ms: 1.05x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.01 ms: 1.01x faster                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.45 ms: 1.04x faster                                  |
| django_template | 32.3 ms                                                | 31.5 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                   |
| deltablue               | 3.66 ms                                                | 3.24 ms: 1.13x faster                                  |
| pycparser               | 1.19 sec                                               | 1.06 sec: 1.12x faster                                 |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.18 ms: 1.10x faster                                  |
| regex_compile           | 136 ms                                                 | 126 ms: 1.08x faster                                   |
| go                      | 140 ms                                                 | 130 ms: 1.08x faster                                   |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                   |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| hexiom                  | 6.34 ms                                                | 5.92 ms: 1.07x faster                                  |
| logging_simple          | 6.02 us                                                | 5.67 us: 1.06x faster                                  |
| float                   | 76.8 ms                                                | 72.4 ms: 1.06x faster                                  |
| logging_silent          | 98.0 ns                                                | 92.5 ns: 1.06x faster                                  |
| tornado_http            | 96.5 ms                                                | 91.3 ms: 1.06x faster                                  |
| chaos                   | 68.7 ms                                                | 65.0 ms: 1.06x faster                                  |
| sympy_expand            | 475 ms                                                 | 450 ms: 1.06x faster                                   |
| thrift                  | 760 us                                                 | 720 us: 1.06x faster                                   |
| pyflate                 | 419 ms                                                 | 398 ms: 1.05x faster                                   |
| python_startup          | 8.58 ms                                                | 8.16 ms: 1.05x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.6 ms: 1.05x faster                                  |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                   |
| json_dumps              | 12.4 ms                                                | 11.8 ms: 1.05x faster                                  |
| sympy_str               | 291 ms                                                 | 279 ms: 1.05x faster                                   |
| dulwich_log             | 64.0 ms                                                | 61.2 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| mako                    | 9.83 ms                                                | 9.45 ms: 1.04x faster                                  |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                   |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.04x faster                                   |
| json                    | 4.87 ms                                                | 4.69 ms: 1.04x faster                                  |
| scimark_lu              | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| meteor_contest          | 104 ms                                                 | 101 ms: 1.04x faster                                   |
| nqueens                 | 83.8 ms                                                | 80.8 ms: 1.04x faster                                  |
| html5lib                | 64.8 ms                                                | 62.6 ms: 1.04x faster                                  |
| django_template         | 32.3 ms                                                | 31.5 ms: 1.03x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 156 ms: 1.03x faster                                   |
| richards                | 46.1 ms                                                | 45.0 ms: 1.03x faster                                  |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| logging_format          | 6.48 us                                                | 6.35 us: 1.02x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.3 ms: 1.02x faster                                  |
| raytrace                | 291 ms                                                 | 286 ms: 1.02x faster                                   |
| fannkuch                | 384 ms                                                 | 378 ms: 1.02x faster                                   |
| chameleon               | 6.38 ms                                                | 6.30 ms: 1.01x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 53.3 ms: 1.01x faster                                  |
| regex_v8                | 22.2 ms                                                | 22.1 ms: 1.01x faster                                  |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                  |
| pickle_list             | 4.14 us                                                | 4.12 us: 1.01x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.01 ms: 1.01x faster                                  |
| spectral_norm           | 98.1 ms                                                | 97.7 ms: 1.00x faster                                  |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                  |
| telco                   | 6.43 ms                                                | 6.51 ms: 1.01x slower                                  |
| pickle_dict             | 31.2 us                                                | 31.6 us: 1.01x slower                                  |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                   |
| regex_effbot            | 3.46 ms                                                | 3.54 ms: 1.02x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 46.4 ns: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                  |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): unpickle, xml_etree_iterparse, xml_etree_generate, nbody
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
