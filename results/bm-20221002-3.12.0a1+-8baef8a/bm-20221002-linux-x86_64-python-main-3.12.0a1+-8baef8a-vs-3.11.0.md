
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8baef8a
- commit date: 2022-10-02
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                   |
| html5lib       | 64.8 ms                                                | 59.3 ms: 1.09x faster                                  |
| tornado_http   | 96.5 ms                                                | 92.8 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.0 ms: 1.07x faster                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| nbody          | 90.0 ms                                                | 96.2 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.08x faster                                   |
| regex_effbot   | 3.46 ms                                                | 3.32 ms: 1.04x faster                                  |
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.04x faster                                  |
| regex_dna      | 203 ms                                                 | 204 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.56 ms: 1.29x faster                                  |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                   |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 157 ms: 1.02x faster                                   |
| pickle_list          | 4.14 us                                                | 4.06 us: 1.02x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.9 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 75.3 ms: 1.01x faster                                  |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.35 ms: 1.03x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.05 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 48.4 ms: 1.06x faster                                  |
| mako           | 9.83 ms                                                | 9.35 ms: 1.05x faster                                  |
| genshi_text    | 21.5 ms                                                | 20.7 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.56 ms: 1.29x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                   |
| deltablue               | 3.66 ms                                                | 3.26 ms: 1.12x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.17 ms: 1.10x faster                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| coroutines              | 26.2 ms                                                | 23.9 ms: 1.10x faster                                  |
| html5lib                | 64.8 ms                                                | 59.3 ms: 1.09x faster                                  |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                   |
| json                    | 4.87 ms                                                | 4.51 ms: 1.08x faster                                  |
| regex_compile           | 136 ms                                                 | 127 ms: 1.08x faster                                   |
| mdp                     | 2.63 sec                                               | 2.45 sec: 1.07x faster                                 |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.07x faster                                 |
| deepcopy_memo           | 35.8 us                                                | 33.6 us: 1.07x faster                                  |
| float                   | 76.8 ms                                                | 72.0 ms: 1.07x faster                                  |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                   |
| genshi_xml              | 51.4 ms                                                | 48.4 ms: 1.06x faster                                  |
| spectral_norm           | 98.1 ms                                                | 92.3 ms: 1.06x faster                                  |
| logging_silent          | 98.0 ns                                                | 92.6 ns: 1.06x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.00 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                 |
| nqueens                 | 83.8 ms                                                | 79.3 ms: 1.06x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                   |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.86 us: 1.05x faster                                  |
| deepcopy                | 341 us                                                 | 324 us: 1.05x faster                                   |
| mako                    | 9.83 ms                                                | 9.35 ms: 1.05x faster                                  |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                   |
| logging_simple          | 6.02 us                                                | 5.75 us: 1.05x faster                                  |
| raytrace                | 291 ms                                                 | 278 ms: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                   |
| dulwich_log             | 64.0 ms                                                | 61.3 ms: 1.04x faster                                  |
| richards                | 46.1 ms                                                | 44.2 ms: 1.04x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.32 ms: 1.04x faster                                  |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.04x faster                                  |
| tornado_http            | 96.5 ms                                                | 92.8 ms: 1.04x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 72.8 ms: 1.04x faster                                  |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 65.6 ms: 1.04x faster                                  |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                   |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| pylint                  | 462 ms                                                 | 447 ms: 1.03x faster                                   |
| chaos                   | 68.7 ms                                                | 66.4 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                  |
| coverage                | 99.3 ms                                                | 96.6 ms: 1.03x faster                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.32 ms: 1.03x faster                                  |
| python_startup          | 8.58 ms                                                | 8.35 ms: 1.03x faster                                  |
| async_tree_none         | 526 ms                                                 | 512 ms: 1.03x faster                                   |
| scimark_fft             | 325 ms                                                 | 317 ms: 1.03x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 43.5 ns: 1.02x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 157 ms: 1.02x faster                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.61 ms: 1.02x faster                                  |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_list             | 4.14 us                                                | 4.06 us: 1.02x faster                                  |
| thrift                  | 760 us                                                 | 744 us: 1.02x faster                                   |
| generators              | 73.5 ms                                                | 72.1 ms: 1.02x faster                                  |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| telco                   | 6.43 ms                                                | 6.33 ms: 1.02x faster                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 52.9 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| logging_format          | 6.48 us                                                | 6.39 us: 1.01x faster                                  |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 75.3 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 730 ms: 1.01x faster                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.05 ms: 1.00x slower                                  |
| regex_dna               | 203 ms                                                 | 204 ms: 1.01x slower                                   |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 640 ms: 1.03x slower                                   |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.04x slower                                  |
| nbody                   | 90.0 ms                                                | 96.2 ms: 1.07x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (6): unpickle_list, chameleon, scimark_lu, async_tree_io, django_template, unpickle
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221002-3.12.0a1+-8baef8a/bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a.json: mypy
