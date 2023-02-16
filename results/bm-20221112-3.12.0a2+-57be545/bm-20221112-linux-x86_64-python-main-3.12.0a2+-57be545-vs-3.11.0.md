
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 57be545
- commit date: 2022-11-12
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.06x faster                                   |
| chameleon      | 6.38 ms                                                | 6.49 ms: 1.02x slower                                  |
| html5lib       | 64.8 ms                                                | 58.9 ms: 1.10x faster                                  |
| tornado_http   | 96.5 ms                                                | 92.5 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.3 ms: 1.05x faster                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                   |
| nbody          | 90.0 ms                                                | 93.4 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                   |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.64 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                  |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.14x faster                                   |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                   |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| unpickle_list        | 4.99 us                                                | 4.91 us: 1.01x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 53.0 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_dict          | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.8 ms: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.52 ms: 1.01x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.24 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.8 ms: 1.10x faster                                  |
| mako            | 9.83 ms                                                | 9.70 ms: 1.01x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.3 ms: 1.01x faster                                  |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.14x faster                                   |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                  |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| richards                | 46.1 ms                                                | 41.7 ms: 1.11x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.16 ms: 1.10x faster                                  |
| html5lib                | 64.8 ms                                                | 58.9 ms: 1.10x faster                                  |
| genshi_xml              | 51.4 ms                                                | 46.8 ms: 1.10x faster                                  |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                   |
| coroutines              | 26.2 ms                                                | 24.1 ms: 1.08x faster                                  |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                   |
| logging_silent          | 98.0 ns                                                | 91.8 ns: 1.07x faster                                  |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.06x faster                                 |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.06x faster                                 |
| 2to3                    | 259 ms                                                 | 246 ms: 1.06x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                  |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                   |
| aiohttp                 | 1.05 ms                                                | 998 us: 1.05x faster                                   |
| float                   | 76.8 ms                                                | 73.3 ms: 1.05x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.1 ms: 1.05x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.5 ms: 1.04x faster                                  |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                  |
| tornado_http            | 96.5 ms                                                | 92.5 ms: 1.04x faster                                  |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                  |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 65.5 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| json                    | 4.87 ms                                                | 4.71 ms: 1.03x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.13 ms: 1.03x faster                                  |
| nqueens                 | 83.8 ms                                                | 81.1 ms: 1.03x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| spectral_norm           | 98.1 ms                                                | 95.2 ms: 1.03x faster                                  |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                 |
| fannkuch                | 384 ms                                                 | 374 ms: 1.03x faster                                   |
| pprint_safe_repr        | 706 ms                                                 | 688 ms: 1.03x faster                                   |
| chaos                   | 68.7 ms                                                | 67.0 ms: 1.03x faster                                  |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                  |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                   |
| telco                   | 6.43 ms                                                | 6.32 ms: 1.02x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.91 us: 1.01x faster                                  |
| mako                    | 9.83 ms                                                | 9.70 ms: 1.01x faster                                  |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 53.0 ms: 1.01x faster                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.35 ms: 1.01x faster                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.64 ms: 1.01x faster                                  |
| genshi_text             | 21.5 ms                                                | 21.3 ms: 1.01x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 75.1 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| python_startup          | 8.58 ms                                                | 8.52 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 731 ms: 1.01x faster                                   |
| pickle_dict             | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                   |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                  |
| coverage                | 99.3 ms                                                | 99.8 ms: 1.01x slower                                  |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                   |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| xml_etree_generate      | 75.9 ms                                                | 76.8 ms: 1.01x slower                                  |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                  |
| chameleon               | 6.38 ms                                                | 6.49 ms: 1.02x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.24 ms: 1.03x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 646 ms: 1.03x slower                                   |
| nbody                   | 90.0 ms                                                | 93.4 ms: 1.04x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.64 ms: 1.05x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.65 us: 1.07x slower                                  |
| generators              | 73.5 ms                                                | 79.6 ms: 1.08x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): unpack_sequence, meteor_contest, scimark_lu, regex_v8, pickle_list, async_tree_none, unpickle
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221112-3.12.0a2+-57be545/bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545.json: mypy
