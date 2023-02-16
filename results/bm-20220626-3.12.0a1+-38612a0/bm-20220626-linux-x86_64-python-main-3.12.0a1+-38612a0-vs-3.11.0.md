
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 38612a0
- commit date: 2022-06-26
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.45 ms: 1.01x slower                                  |
| html5lib       | 64.8 ms                                                | 62.0 ms: 1.04x faster                                  |
| tornado_http   | 96.5 ms                                                | 92.1 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.1 ms: 1.08x faster                                  |
| pidigits       | 197 ms                                                 | 194 ms: 1.02x faster                                   |
| nbody          | 90.0 ms                                                | 94.8 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.04x faster                                  |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.61 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                   |
| json_loads           | 26.1 us                                                | 24.5 us: 1.06x faster                                  |
| pickle_pure_python   | 308 us                                                 | 294 us: 1.05x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 155 ms: 1.03x faster                                   |
| pickle_dict          | 31.2 us                                                | 30.1 us: 1.03x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.0 ms: 1.03x faster                                  |
| json_dumps           | 12.4 ms                                                | 12.0 ms: 1.03x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.91 us: 1.01x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 75.0 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.26 ms: 1.04x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.10 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.46 ms: 1.04x faster                                  |
| django_template | 32.3 ms                                                | 31.6 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.89 ms: 1.18x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                   |
| pycparser               | 1.19 sec                                               | 1.05 sec: 1.13x faster                                 |
| deltablue               | 3.66 ms                                                | 3.24 ms: 1.13x faster                                  |
| logging_silent          | 98.0 ns                                                | 89.6 ns: 1.09x faster                                  |
| go                      | 140 ms                                                 | 128 ms: 1.09x faster                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 62.4 ms: 1.09x faster                                  |
| float                   | 76.8 ms                                                | 71.1 ms: 1.08x faster                                  |
| chaos                   | 68.7 ms                                                | 63.8 ms: 1.08x faster                                  |
| scimark_fft             | 325 ms                                                 | 304 ms: 1.07x faster                                   |
| hexiom                  | 6.34 ms                                                | 5.94 ms: 1.07x faster                                  |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                   |
| json_loads              | 26.1 us                                                | 24.5 us: 1.06x faster                                  |
| spectral_norm           | 98.1 ms                                                | 92.8 ms: 1.06x faster                                  |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                   |
| sympy_str               | 291 ms                                                 | 277 ms: 1.05x faster                                   |
| pickle_pure_python      | 308 us                                                 | 294 us: 1.05x faster                                   |
| tornado_http            | 96.5 ms                                                | 92.1 ms: 1.05x faster                                  |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                   |
| raytrace                | 291 ms                                                 | 279 ms: 1.05x faster                                   |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.04x faster                                  |
| html5lib                | 64.8 ms                                                | 62.0 ms: 1.04x faster                                  |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                   |
| scimark_lu              | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| unpack_sequence         | 44.5 ns                                                | 42.8 ns: 1.04x faster                                  |
| mako                    | 9.83 ms                                                | 9.46 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| python_startup          | 8.58 ms                                                | 8.26 ms: 1.04x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.7 ms: 1.04x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 155 ms: 1.03x faster                                   |
| pickle_dict             | 31.2 us                                                | 30.1 us: 1.03x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 52.0 ms: 1.03x faster                                  |
| json                    | 4.87 ms                                                | 4.72 ms: 1.03x faster                                  |
| json_dumps              | 12.4 ms                                                | 12.0 ms: 1.03x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                  |
| django_template         | 32.3 ms                                                | 31.6 ms: 1.02x faster                                  |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| fannkuch                | 384 ms                                                 | 376 ms: 1.02x faster                                   |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                   |
| nqueens                 | 83.8 ms                                                | 82.2 ms: 1.02x faster                                  |
| pidigits                | 197 ms                                                 | 194 ms: 1.02x faster                                   |
| richards                | 46.1 ms                                                | 45.4 ms: 1.02x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.91 us: 1.01x faster                                  |
| logging_format          | 6.48 us                                                | 6.40 us: 1.01x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 75.0 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.10 ms: 1.01x slower                                  |
| chameleon               | 6.38 ms                                                | 6.45 ms: 1.01x slower                                  |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                   |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.04x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.61 ms: 1.04x slower                                  |
| nbody                   | 90.0 ms                                                | 94.8 ms: 1.05x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (4): pickle_list, telco, pathlib, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
