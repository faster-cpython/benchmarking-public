
# Results vs. base

- fork: penguin-wwy
- ref: add_return_none
- machine: linux-x86_64
- commit hash: f1deb5c
- commit date: 2023-02-07
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.01x faster                                                     |
| chameleon      | 6.43 ms                                                                | 6.36 ms: 1.01x faster                                                    |
| docutils       | 2.51 sec                                                               | 2.49 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 73.3 ms                                                                | 72.1 ms: 1.02x faster                                                    |
| nbody          | 96.4 ms                                                                | 95.5 ms: 1.01x faster                                                    |
| pidigits       | 192 ms                                                                 | 197 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                                 | 200 ms: 1.06x faster                                                     |
| regex_v8       | 22.1 ms                                                                | 21.2 ms: 1.04x faster                                                    |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                     |
| regex_effbot   | 3.34 ms                                                                | 3.50 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle               | 10.6 us                                                                | 9.99 us: 1.06x faster                                                    |
| unpickle             | 13.6 us                                                                | 13.1 us: 1.04x faster                                                    |
| pickle_dict          | 31.7 us                                                                | 30.6 us: 1.04x faster                                                    |
| pickle_list          | 4.21 us                                                                | 4.07 us: 1.04x faster                                                    |
| unpickle_pure_python | 200 us                                                                 | 198 us: 1.01x faster                                                     |
| json_dumps           | 9.42 ms                                                                | 9.37 ms: 1.00x faster                                                    |
| xml_etree_process    | 53.2 ms                                                                | 53.5 ms: 1.00x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (6): unpickle_list, xml_etree_generate, pickle_pure_python, xml_etree_iterparse, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.96 ms                                                                | 8.90 ms: 1.01x faster                                                    |
| python_startup_no_site | 6.48 ms                                                                | 6.46 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 9.85 ms                                                                | 9.63 ms: 1.02x faster                                                    |
| genshi_text    | 20.8 ms                                                                | 20.5 ms: 1.02x faster                                                    |
| genshi_xml     | 46.8 ms                                                                | 46.6 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal            | 3.96 ms                                                                | 3.52 ms: 1.13x faster                                                    |
| regex_dna               | 212 ms                                                                 | 200 ms: 1.06x faster                                                     |
| pickle                  | 10.6 us                                                                | 9.99 us: 1.06x faster                                                    |
| regex_v8                | 22.1 ms                                                                | 21.2 ms: 1.04x faster                                                    |
| pprint_safe_repr        | 694 ms                                                                 | 668 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.42 sec                                                               | 1.37 sec: 1.04x faster                                                   |
| unpickle                | 13.6 us                                                                | 13.1 us: 1.04x faster                                                    |
| pickle_dict             | 31.7 us                                                                | 30.6 us: 1.04x faster                                                    |
| pickle_list             | 4.21 us                                                                | 4.07 us: 1.04x faster                                                    |
| pycparser               | 1.14 sec                                                               | 1.11 sec: 1.03x faster                                                   |
| sqlalchemy_imperative   | 18.1 ms                                                                | 17.5 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult | 4.14 ms                                                                | 4.01 ms: 1.03x faster                                                    |
| deltablue               | 3.25 ms                                                                | 3.16 ms: 1.03x faster                                                    |
| mako                    | 9.85 ms                                                                | 9.63 ms: 1.02x faster                                                    |
| logging_silent          | 92.3 ns                                                                | 90.7 ns: 1.02x faster                                                    |
| gunicorn                | 1.09 ms                                                                | 1.07 ms: 1.02x faster                                                    |
| float                   | 73.3 ms                                                                | 72.1 ms: 1.02x faster                                                    |
| genshi_text             | 20.8 ms                                                                | 20.5 ms: 1.02x faster                                                    |
| scimark_fft             | 307 ms                                                                 | 303 ms: 1.01x faster                                                     |
| scimark_monte_carlo     | 66.2 ms                                                                | 65.3 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.71 ms                                                                | 1.69 ms: 1.01x faster                                                    |
| async_generators        | 353 ms                                                                 | 349 ms: 1.01x faster                                                     |
| thrift                  | 747 us                                                                 | 739 us: 1.01x faster                                                     |
| dulwich_log             | 62.9 ms                                                                | 62.2 ms: 1.01x faster                                                    |
| chameleon               | 6.43 ms                                                                | 6.36 ms: 1.01x faster                                                    |
| sqlite_synth            | 2.61 us                                                                | 2.58 us: 1.01x faster                                                    |
| regex_compile           | 128 ms                                                                 | 127 ms: 1.01x faster                                                     |
| crypto_pyaes            | 74.0 ms                                                                | 73.2 ms: 1.01x faster                                                    |
| nbody                   | 96.4 ms                                                                | 95.5 ms: 1.01x faster                                                    |
| richards                | 42.3 ms                                                                | 41.9 ms: 1.01x faster                                                    |
| sympy_str               | 271 ms                                                                 | 269 ms: 1.01x faster                                                     |
| telco                   | 6.39 ms                                                                | 6.33 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 2.98 us                                                                | 2.95 us: 1.01x faster                                                    |
| sqlglot_parse           | 1.42 ms                                                                | 1.40 ms: 1.01x faster                                                    |
| create_gc_cycles        | 1.47 ms                                                                | 1.46 ms: 1.01x faster                                                    |
| docutils                | 2.51 sec                                                               | 2.49 sec: 1.01x faster                                                   |
| generators              | 76.2 ms                                                                | 75.6 ms: 1.01x faster                                                    |
| unpickle_pure_python    | 200 us                                                                 | 198 us: 1.01x faster                                                     |
| python_startup          | 8.96 ms                                                                | 8.90 ms: 1.01x faster                                                    |
| 2to3                    | 252 ms                                                                 | 251 ms: 1.01x faster                                                     |
| bench_thread_pool       | 784 us                                                                 | 780 us: 1.01x faster                                                     |
| sympy_expand            | 456 ms                                                                 | 454 ms: 1.01x faster                                                     |
| logging_simple          | 5.72 us                                                                | 5.69 us: 1.01x faster                                                    |
| json_dumps              | 9.42 ms                                                                | 9.37 ms: 1.00x faster                                                    |
| mdp                     | 2.62 sec                                                               | 2.60 sec: 1.00x faster                                                   |
| deepcopy                | 333 us                                                                 | 332 us: 1.00x faster                                                     |
| genshi_xml              | 46.8 ms                                                                | 46.6 ms: 1.00x faster                                                    |
| python_startup_no_site  | 6.48 ms                                                                | 6.46 ms: 1.00x faster                                                    |
| aiohttp                 | 998 us                                                                 | 995 us: 1.00x faster                                                     |
| sqlglot_optimize        | 50.9 ms                                                                | 51.0 ms: 1.00x slower                                                    |
| xml_etree_process       | 53.2 ms                                                                | 53.5 ms: 1.00x slower                                                    |
| pathlib                 | 17.5 ms                                                                | 17.7 ms: 1.01x slower                                                    |
| fannkuch                | 367 ms                                                                 | 370 ms: 1.01x slower                                                     |
| raytrace                | 282 ms                                                                 | 285 ms: 1.01x slower                                                     |
| nqueens                 | 76.7 ms                                                                | 77.8 ms: 1.01x slower                                                    |
| json                    | 4.58 ms                                                                | 4.66 ms: 1.02x slower                                                    |
| pyflate                 | 400 ms                                                                 | 406 ms: 1.02x slower                                                     |
| unpack_sequence         | 42.3 ns                                                                | 43.0 ns: 1.02x slower                                                    |
| async_tree_io           | 1.30 sec                                                               | 1.33 sec: 1.02x slower                                                   |
| meteor_contest          | 104 ms                                                                 | 106 ms: 1.02x slower                                                     |
| pidigits                | 192 ms                                                                 | 197 ms: 1.03x slower                                                     |
| coverage                | 95.9 ms                                                                | 98.4 ms: 1.03x slower                                                    |
| async_tree_memoization  | 638 ms                                                                 | 667 ms: 1.05x slower                                                     |
| regex_effbot            | 3.34 ms                                                                | 3.50 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (28): html5lib, scimark_sor, scimark_lu, mypy, tornado_http, djangocms, go, unpickle_list, hexiom, sqlglot_normalize, sympy_sum, deepcopy_memo, sympy_integrate, xml_etree_generate, pickle_pure_python, chaos, logging_format, xml_etree_iterparse, bench_mp_pool, asyncio_tcp, xml_etree_parse, sqlalchemy_declarative, coroutines, django_template, async_tree_none, async_tree_cpu_io_mixed, spectral_norm, json_loads
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230206-3.12.0a4+-d3e2dd6/bm-20230206-linux-x86_64-python-d3e2dd6e71bd8e548297-3.12.0a4+-d3e2dd6.json: dask
