
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 660f102
- commit date: 2022-10-15
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.71 ms: 1.05x slower                                  |
| html5lib       | 64.8 ms                                                | 59.2 ms: 1.09x faster                                  |
| tornado_http   | 96.5 ms                                                | 92.6 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                  |
| pidigits       | 197 ms                                                 | 199 ms: 1.01x slower                                   |
| nbody          | 90.0 ms                                                | 94.2 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| regex_dna      | 203 ms                                                 | 200 ms: 1.01x faster                                   |
| regex_effbot   | 3.46 ms                                                | 3.60 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.60 ms: 1.29x faster                                  |
| unpickle_pure_python | 227 us                                                 | 202 us: 1.12x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 145 ms: 1.10x faster                                   |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                  |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                   |
| unpickle             | 13.3 us                                                | 12.9 us: 1.03x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                  |
| pickle_dict          | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.9 ms: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): pickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.41 ms: 1.02x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.09 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.2 ms: 1.04x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.0 ms: 1.02x faster                                  |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.60 ms: 1.29x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 202 us: 1.12x faster                                   |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 145 ms: 1.10x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.16 ms: 1.10x faster                                  |
| deltablue               | 3.66 ms                                                | 3.31 ms: 1.10x faster                                  |
| html5lib                | 64.8 ms                                                | 59.2 ms: 1.09x faster                                  |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                  |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                 |
| richards                | 46.1 ms                                                | 43.0 ms: 1.07x faster                                  |
| coroutines              | 26.2 ms                                                | 24.6 ms: 1.06x faster                                  |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| pprint_safe_repr        | 706 ms                                                 | 669 ms: 1.06x faster                                   |
| logging_silent          | 98.0 ns                                                | 92.9 ns: 1.05x faster                                  |
| nqueens                 | 83.8 ms                                                | 79.5 ms: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 997 us: 1.05x faster                                   |
| dulwich_log             | 64.0 ms                                                | 60.9 ms: 1.05x faster                                  |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                   |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                  |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                   |
| hexiom                  | 6.34 ms                                                | 6.05 ms: 1.05x faster                                  |
| genshi_xml              | 51.4 ms                                                | 49.2 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| fannkuch                | 384 ms                                                 | 368 ms: 1.04x faster                                   |
| tornado_http            | 96.5 ms                                                | 92.6 ms: 1.04x faster                                  |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                   |
| chaos                   | 68.7 ms                                                | 66.1 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                  |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| mdp                     | 2.63 sec                                               | 2.54 sec: 1.04x faster                                 |
| scimark_monte_carlo     | 68.0 ms                                                | 65.6 ms: 1.04x faster                                  |
| deepcopy_memo           | 35.8 us                                                | 34.6 us: 1.03x faster                                  |
| scimark_fft             | 325 ms                                                 | 315 ms: 1.03x faster                                   |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| unpickle                | 13.3 us                                                | 12.9 us: 1.03x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 51.5 ms: 1.02x faster                                  |
| genshi_text             | 21.5 ms                                                | 21.0 ms: 1.02x faster                                  |
| thrift                  | 760 us                                                 | 742 us: 1.02x faster                                   |
| generators              | 73.5 ms                                                | 71.8 ms: 1.02x faster                                  |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                   |
| python_startup          | 8.58 ms                                                | 8.41 ms: 1.02x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| json                    | 4.87 ms                                                | 4.78 ms: 1.02x faster                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.34 ms: 1.02x faster                                  |
| logging_format          | 6.48 us                                                | 6.38 us: 1.02x faster                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.01x faster                                   |
| spectral_norm           | 98.1 ms                                                | 96.7 ms: 1.01x faster                                  |
| regex_dna               | 203 ms                                                 | 200 ms: 1.01x faster                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.63 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| coverage                | 99.3 ms                                                | 98.4 ms: 1.01x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 44.1 ns: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 730 ms: 1.01x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 75.2 ms: 1.01x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                  |
| pickle_dict             | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.09 ms: 1.01x slower                                  |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                  |
| pidigits                | 197 ms                                                 | 199 ms: 1.01x slower                                   |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                   |
| xml_etree_generate      | 75.9 ms                                                | 76.9 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| async_tree_memoization  | 624 ms                                                 | 647 ms: 1.04x slower                                   |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.60 ms: 1.04x slower                                  |
| nbody                   | 90.0 ms                                                | 94.2 ms: 1.05x slower                                  |
| chameleon               | 6.38 ms                                                | 6.71 ms: 1.05x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.05x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): pylint, pickle_list, mako, regex_v8, scimark_lu, xml_etree_process, telco
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221015-3.12.0a1+-660f102/bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102.json: mypy
