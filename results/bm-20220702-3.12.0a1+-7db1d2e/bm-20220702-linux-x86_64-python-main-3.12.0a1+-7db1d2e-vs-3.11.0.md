
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7db1d2e
- commit date: 2022-07-02
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| html5lib       | 64.8 ms                                                | 62.0 ms: 1.05x faster                                  |
| tornado_http   | 96.5 ms                                                | 91.4 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 69.9 ms: 1.10x faster                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 125 ms: 1.09x faster                                   |
| regex_dna      | 203 ms                                                 | 197 ms: 1.03x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.0 ms: 1.01x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.49 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                   |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                   |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                  |
| json_dumps           | 12.4 ms                                                | 11.9 ms: 1.03x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.0 ms: 1.03x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 156 ms: 1.02x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.02x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 75.0 ms: 1.01x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                  |
| pickle_list          | 4.14 us                                                | 4.28 us: 1.03x slower                                  |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.22 ms: 1.04x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.07 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.55 ms: 1.03x faster                                  |
| django_template | 32.3 ms                                                | 32.0 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220702-linux-x86_64-python-main-3.12.0a1+-7db1d2e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                   |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                  |
| float                   | 76.8 ms                                                | 69.9 ms: 1.10x faster                                  |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.10x faster                                 |
| regex_compile           | 136 ms                                                 | 125 ms: 1.09x faster                                   |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.21 ms: 1.09x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 62.8 ms: 1.08x faster                                  |
| hexiom                  | 6.34 ms                                                | 5.88 ms: 1.08x faster                                  |
| go                      | 140 ms                                                 | 130 ms: 1.08x faster                                   |
| pyflate                 | 419 ms                                                 | 389 ms: 1.08x faster                                   |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                  |
| logging_silent          | 98.0 ns                                                | 91.7 ns: 1.07x faster                                  |
| sympy_expand            | 475 ms                                                 | 450 ms: 1.06x faster                                   |
| tornado_http            | 96.5 ms                                                | 91.4 ms: 1.06x faster                                  |
| sympy_str               | 291 ms                                                 | 276 ms: 1.05x faster                                   |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                   |
| chaos                   | 68.7 ms                                                | 65.2 ms: 1.05x faster                                  |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                  |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                   |
| html5lib                | 64.8 ms                                                | 62.0 ms: 1.05x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.2 ms: 1.04x faster                                  |
| python_startup          | 8.58 ms                                                | 8.22 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| spectral_norm           | 98.1 ms                                                | 94.3 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| json                    | 4.87 ms                                                | 4.70 ms: 1.04x faster                                  |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.04x faster                                   |
| regex_dna               | 203 ms                                                 | 197 ms: 1.03x faster                                   |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                  |
| json_dumps              | 12.4 ms                                                | 11.9 ms: 1.03x faster                                  |
| nqueens                 | 83.8 ms                                                | 81.0 ms: 1.03x faster                                  |
| richards                | 46.1 ms                                                | 44.6 ms: 1.03x faster                                  |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 73.3 ms: 1.03x faster                                  |
| scimark_lu              | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 52.0 ms: 1.03x faster                                  |
| meteor_contest          | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| fannkuch                | 384 ms                                                 | 373 ms: 1.03x faster                                   |
| mako                    | 9.83 ms                                                | 9.55 ms: 1.03x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 156 ms: 1.02x faster                                   |
| thrift                  | 760 us                                                 | 744 us: 1.02x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.02x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 75.0 ms: 1.01x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                  |
| regex_v8                | 22.2 ms                                                | 22.0 ms: 1.01x faster                                  |
| django_template         | 32.3 ms                                                | 32.0 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.07 ms: 1.00x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.49 ms: 1.01x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 45.5 ns: 1.02x slower                                  |
| telco                   | 6.43 ms                                                | 6.59 ms: 1.03x slower                                  |
| pickle_list             | 4.14 us                                                | 4.28 us: 1.03x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                  |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (3): nbody, chameleon, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
