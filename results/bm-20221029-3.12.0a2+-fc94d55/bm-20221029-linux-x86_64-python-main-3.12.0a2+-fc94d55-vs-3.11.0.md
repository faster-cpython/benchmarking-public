
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: fc94d55
- commit date: 2022-10-29
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| html5lib       | 64.8 ms                                                | 59.5 ms: 1.09x faster                                  |
| tornado_http   | 96.5 ms                                                | 93.1 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.9 ms: 1.05x faster                                  |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 90.0 ms                                                | 98.1 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.9 ms: 1.03x slower                                  |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.69 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.31 ms: 1.33x faster                                  |
| json_loads           | 26.1 us                                                | 23.5 us: 1.11x faster                                  |
| unpickle_pure_python | 227 us                                                 | 205 us: 1.11x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                   |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                   |
| unpickle             | 13.3 us                                                | 12.9 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| xml_etree_process    | 53.7 ms                                                | 53.1 ms: 1.01x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.1 ms: 1.00x slower                                  |
| pickle_dict          | 31.2 us                                                | 31.6 us: 1.02x slower                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.37 ms: 1.02x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.08 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.2 ms: 1.05x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.1 ms: 1.02x faster                                  |
| mako            | 9.83 ms                                                | 9.72 ms: 1.01x faster                                  |
| django_template | 32.3 ms                                                | 32.0 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.31 ms: 1.33x faster                                  |
| json_loads              | 26.1 us                                                | 23.5 us: 1.11x faster                                  |
| deltablue               | 3.66 ms                                                | 3.30 ms: 1.11x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 205 us: 1.11x faster                                   |
| html5lib                | 64.8 ms                                                | 59.5 ms: 1.09x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                   |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                 |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.27 ms: 1.07x faster                                  |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                   |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                   |
| coroutines              | 26.2 ms                                                | 24.4 ms: 1.07x faster                                  |
| richards                | 46.1 ms                                                | 43.4 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                   |
| float                   | 76.8 ms                                                | 72.9 ms: 1.05x faster                                  |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.05x faster                                  |
| genshi_xml              | 51.4 ms                                                | 49.2 ms: 1.05x faster                                  |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| spectral_norm           | 98.1 ms                                                | 94.1 ms: 1.04x faster                                  |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                  |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                  |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| logging_silent          | 98.0 ns                                                | 94.4 ns: 1.04x faster                                  |
| nqueens                 | 83.8 ms                                                | 80.7 ms: 1.04x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.6 ms: 1.04x faster                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                  |
| tornado_http            | 96.5 ms                                                | 93.1 ms: 1.04x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 65.6 ms: 1.04x faster                                  |
| mdp                     | 2.63 sec                                               | 2.54 sec: 1.04x faster                                 |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                  |
| thrift                  | 760 us                                                 | 736 us: 1.03x faster                                   |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                   |
| fannkuch                | 384 ms                                                 | 373 ms: 1.03x faster                                   |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| unpickle                | 13.3 us                                                | 12.9 us: 1.02x faster                                  |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.02x faster                                  |
| python_startup          | 8.58 ms                                                | 8.37 ms: 1.02x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                  |
| scimark_fft             | 325 ms                                                 | 318 ms: 1.02x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 51.5 ms: 1.02x faster                                  |
| coverage                | 99.3 ms                                                | 97.3 ms: 1.02x faster                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.34 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| telco                   | 6.43 ms                                                | 6.31 ms: 1.02x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                   |
| genshi_text             | 21.5 ms                                                | 21.1 ms: 1.02x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.22 ms: 1.02x faster                                  |
| chaos                   | 68.7 ms                                                | 67.4 ms: 1.02x faster                                  |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 74.7 ms: 1.01x faster                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.63 ms: 1.01x faster                                  |
| generators              | 73.5 ms                                                | 72.6 ms: 1.01x faster                                  |
| mako                    | 9.83 ms                                                | 9.72 ms: 1.01x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 53.1 ms: 1.01x faster                                  |
| logging_format          | 6.48 us                                                | 6.41 us: 1.01x faster                                  |
| django_template         | 32.3 ms                                                | 32.0 ms: 1.01x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.1 ms: 1.00x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.08 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| pickle_dict             | 31.2 us                                                | 31.6 us: 1.02x slower                                  |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                   |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                   |
| async_tree_memoization  | 624 ms                                                 | 638 ms: 1.02x slower                                   |
| regex_v8                | 22.2 ms                                                | 22.9 ms: 1.03x slower                                  |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                   |
| unpack_sequence         | 44.5 ns                                                | 46.0 ns: 1.04x slower                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.06x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.69 ms: 1.07x slower                                  |
| nbody                   | 90.0 ms                                                | 98.1 ms: 1.09x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (5): pylint, unpickle_list, chameleon, async_tree_cpu_io_mixed, pickle_list
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221029-3.12.0a2+-fc94d55/bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55.json: mypy
