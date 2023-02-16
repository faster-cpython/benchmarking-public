
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c20186c
- commit date: 2022-07-17
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.28 ms: 1.02x faster                                  |
| html5lib       | 64.8 ms                                                | 62.8 ms: 1.03x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.3 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.0 ms: 1.07x faster                                  |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 90.0 ms                                                | 88.8 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| regex_v8       | 22.2 ms                                                | 20.9 ms: 1.06x faster                                  |
| regex_dna      | 203 ms                                                 | 197 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 227 us                                                 | 202 us: 1.13x faster                                   |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                   |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                  |
| json_dumps           | 12.4 ms                                                | 11.9 ms: 1.04x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.2 ms: 1.03x faster                                  |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 75.2 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                  |
| pickle_list          | 4.14 us                                                | 4.24 us: 1.02x slower                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.17 ms: 1.05x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.02 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.33 ms: 1.05x faster                                  |
| django_template | 32.3 ms                                                | 32.1 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220717-linux-x86_64-python-main-3.12.0a1+-c20186c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.04 ms: 1.14x faster                                  |
| pycparser               | 1.19 sec                                               | 1.05 sec: 1.13x faster                                 |
| unpickle_pure_python    | 227 us                                                 | 202 us: 1.13x faster                                   |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                   |
| logging_simple          | 6.02 us                                                | 5.61 us: 1.07x faster                                  |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                  |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| logging_silent          | 98.0 ns                                                | 91.9 ns: 1.07x faster                                  |
| float                   | 76.8 ms                                                | 72.0 ms: 1.07x faster                                  |
| regex_v8                | 22.2 ms                                                | 20.9 ms: 1.06x faster                                  |
| nqueens                 | 83.8 ms                                                | 78.8 ms: 1.06x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                   |
| tornado_http            | 96.5 ms                                                | 91.3 ms: 1.06x faster                                  |
| json                    | 4.87 ms                                                | 4.61 ms: 1.06x faster                                  |
| mako                    | 9.83 ms                                                | 9.33 ms: 1.05x faster                                  |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                   |
| dulwich_log             | 64.0 ms                                                | 60.8 ms: 1.05x faster                                  |
| spectral_norm           | 98.1 ms                                                | 93.4 ms: 1.05x faster                                  |
| python_startup          | 8.58 ms                                                | 8.17 ms: 1.05x faster                                  |
| sympy_str               | 291 ms                                                 | 278 ms: 1.05x faster                                   |
| hexiom                  | 6.34 ms                                                | 6.05 ms: 1.05x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 65.1 ms: 1.04x faster                                  |
| pyflate                 | 419 ms                                                 | 401 ms: 1.04x faster                                   |
| sympy_sum               | 166 ms                                                 | 159 ms: 1.04x faster                                   |
| json_dumps              | 12.4 ms                                                | 11.9 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| logging_format          | 6.48 us                                                | 6.22 us: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 72.9 ms: 1.04x faster                                  |
| chaos                   | 68.7 ms                                                | 66.2 ms: 1.04x faster                                  |
| regex_dna               | 203 ms                                                 | 197 ms: 1.03x faster                                   |
| richards                | 46.1 ms                                                | 44.7 ms: 1.03x faster                                  |
| html5lib                | 64.8 ms                                                | 62.8 ms: 1.03x faster                                  |
| fannkuch                | 384 ms                                                 | 373 ms: 1.03x faster                                   |
| unpack_sequence         | 44.5 ns                                                | 43.2 ns: 1.03x faster                                  |
| meteor_contest          | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| thrift                  | 760 us                                                 | 739 us: 1.03x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 52.2 ms: 1.03x faster                                  |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                  |
| chameleon               | 6.38 ms                                                | 6.28 ms: 1.02x faster                                  |
| nbody                   | 90.0 ms                                                | 88.8 ms: 1.01x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 75.2 ms: 1.01x faster                                  |
| django_template         | 32.3 ms                                                | 32.1 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.02 ms: 1.00x faster                                  |
| telco                   | 6.43 ms                                                | 6.50 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                  |
| scimark_sor             | 115 ms                                                 | 117 ms: 1.02x slower                                   |
| pickle_list             | 4.14 us                                                | 4.24 us: 1.02x slower                                  |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (3): xml_etree_parse, regex_effbot, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
