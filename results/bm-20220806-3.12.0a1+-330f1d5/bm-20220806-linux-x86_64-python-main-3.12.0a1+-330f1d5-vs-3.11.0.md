
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 330f1d5
- commit date: 2022-08-06
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.50 ms: 1.02x slower                                  |
| html5lib       | 64.8 ms                                                | 62.6 ms: 1.04x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.7 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.1 ms: 1.04x faster                                  |
| pidigits       | 197 ms                                                 | 194 ms: 1.02x faster                                   |
| nbody          | 90.0 ms                                                | 91.3 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.08x faster                                   |
| regex_v8       | 22.2 ms                                                | 20.8 ms: 1.07x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.50 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                  |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                   |
| pickle_pure_python   | 308 us                                                 | 288 us: 1.07x faster                                   |
| json_loads           | 26.1 us                                                | 24.6 us: 1.06x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.2 ms: 1.03x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 156 ms: 1.03x faster                                   |
| xml_etree_generate   | 75.9 ms                                                | 75.0 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| unpickle_list        | 4.99 us                                                | 5.06 us: 1.02x slower                                  |
| pickle_dict          | 31.2 us                                                | 31.9 us: 1.02x slower                                  |
| pickle_list          | 4.14 us                                                | 4.26 us: 1.03x slower                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.15 ms: 1.05x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.01 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.50 ms: 1.04x faster                                  |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.91 ms: 1.17x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                   |
| pycparser               | 1.19 sec                                               | 1.04 sec: 1.14x faster                                 |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                  |
| logging_silent          | 98.0 ns                                                | 89.9 ns: 1.09x faster                                  |
| regex_compile           | 136 ms                                                 | 127 ms: 1.08x faster                                   |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                   |
| regex_v8                | 22.2 ms                                                | 20.8 ms: 1.07x faster                                  |
| pickle_pure_python      | 308 us                                                 | 288 us: 1.07x faster                                   |
| pyflate                 | 419 ms                                                 | 393 ms: 1.07x faster                                   |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                  |
| json_loads              | 26.1 us                                                | 24.6 us: 1.06x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.2 ms: 1.06x faster                                  |
| nqueens                 | 83.8 ms                                                | 79.2 ms: 1.06x faster                                  |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                  |
| tornado_http            | 96.5 ms                                                | 91.7 ms: 1.05x faster                                  |
| python_startup          | 8.58 ms                                                | 8.15 ms: 1.05x faster                                  |
| raytrace                | 291 ms                                                 | 278 ms: 1.05x faster                                   |
| scimark_fft             | 325 ms                                                 | 311 ms: 1.05x faster                                   |
| spectral_norm           | 98.1 ms                                                | 93.8 ms: 1.05x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.2 ms: 1.05x faster                                  |
| scimark_sor             | 115 ms                                                 | 110 ms: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                  |
| float                   | 76.8 ms                                                | 74.1 ms: 1.04x faster                                  |
| richards                | 46.1 ms                                                | 44.5 ms: 1.04x faster                                  |
| html5lib                | 64.8 ms                                                | 62.6 ms: 1.04x faster                                  |
| json                    | 4.87 ms                                                | 4.70 ms: 1.04x faster                                  |
| mako                    | 9.83 ms                                                | 9.50 ms: 1.04x faster                                  |
| sympy_sum               | 166 ms                                                 | 160 ms: 1.03x faster                                   |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                   |
| meteor_contest          | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 52.2 ms: 1.03x faster                                  |
| chaos                   | 68.7 ms                                                | 66.8 ms: 1.03x faster                                  |
| fannkuch                | 384 ms                                                 | 374 ms: 1.03x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 156 ms: 1.03x faster                                   |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                  |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                   |
| pidigits                | 197 ms                                                 | 194 ms: 1.02x faster                                   |
| thrift                  | 760 us                                                 | 748 us: 1.02x faster                                   |
| xml_etree_generate      | 75.9 ms                                                | 75.0 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.01 ms: 1.00x faster                                  |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| regex_effbot            | 3.46 ms                                                | 3.50 ms: 1.01x slower                                  |
| nbody                   | 90.0 ms                                                | 91.3 ms: 1.01x slower                                  |
| unpickle_list           | 4.99 us                                                | 5.06 us: 1.02x slower                                  |
| chameleon               | 6.38 ms                                                | 6.50 ms: 1.02x slower                                  |
| pickle_dict             | 31.2 us                                                | 31.9 us: 1.02x slower                                  |
| pickle_list             | 4.14 us                                                | 4.26 us: 1.03x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 45.9 ns: 1.03x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (3): telco, regex_dna, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
