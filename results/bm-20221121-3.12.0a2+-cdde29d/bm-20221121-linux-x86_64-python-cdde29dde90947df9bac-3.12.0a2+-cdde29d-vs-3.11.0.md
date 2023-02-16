
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 244 ms: 1.06x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.31 ms: 1.01x faster                                                  |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| html5lib       | 64.8 ms                                                | 59.1 ms: 1.10x faster                                                  |
| tornado_http   | 96.5 ms                                                | 92.8 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.1 ms: 1.05x faster                                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| nbody          | 90.0 ms                                                | 93.7 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                   |
| regex_v8       | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                  |
| regex_effbot   | 3.46 ms                                                | 3.55 ms: 1.03x slower                                                  |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                   |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                   |
| pickle_list          | 4.14 us                                                | 3.97 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| xml_etree_process    | 53.7 ms                                                | 52.8 ms: 1.02x faster                                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.3 ms: 1.01x slower                                                  |
| pickle_dict          | 31.2 us                                                | 31.3 us: 1.01x slower                                                  |
| unpickle             | 13.3 us                                                | 13.6 us: 1.02x slower                                                  |
| unpickle_list        | 4.99 us                                                | 5.13 us: 1.03x slower                                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.48 ms: 1.01x faster                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.12 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.2 ms: 1.07x faster                                                  |
| mako            | 9.83 ms                                                | 9.56 ms: 1.03x faster                                                  |
| django_template | 32.3 ms                                                | 32.1 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                                  |
| deltablue               | 3.66 ms                                                | 3.17 ms: 1.15x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.08 ms: 1.12x faster                                                  |
| richards                | 46.1 ms                                                | 41.3 ms: 1.12x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.07 sec: 1.11x faster                                                 |
| genshi_xml              | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                   |
| html5lib                | 64.8 ms                                                | 59.1 ms: 1.10x faster                                                  |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                   |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.62 us: 1.07x faster                                                  |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                  |
| genshi_text             | 21.5 ms                                                | 20.2 ms: 1.07x faster                                                  |
| 2to3                    | 259 ms                                                 | 244 ms: 1.06x faster                                                   |
| deepcopy_memo           | 35.8 us                                                | 33.8 us: 1.06x faster                                                  |
| scimark_fft             | 325 ms                                                 | 307 ms: 1.06x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                   |
| regex_v8                | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                  |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.05x faster                                                   |
| json                    | 4.87 ms                                                | 4.61 ms: 1.05x faster                                                  |
| pyflate                 | 419 ms                                                 | 397 ms: 1.05x faster                                                   |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                   |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| sqlglot_optimize        | 52.7 ms                                                | 50.2 ms: 1.05x faster                                                  |
| float                   | 76.8 ms                                                | 73.1 ms: 1.05x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                   |
| chaos                   | 68.7 ms                                                | 65.6 ms: 1.05x faster                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 65.0 ms: 1.05x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                   |
| pickle_list             | 4.14 us                                                | 3.97 us: 1.04x faster                                                  |
| logging_silent          | 98.0 ns                                                | 94.1 ns: 1.04x faster                                                  |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                   |
| dulwich_log             | 64.0 ms                                                | 61.5 ms: 1.04x faster                                                  |
| tornado_http            | 96.5 ms                                                | 92.8 ms: 1.04x faster                                                  |
| sympy_str               | 291 ms                                                 | 280 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                   |
| fannkuch                | 384 ms                                                 | 373 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                  |
| logging_format          | 6.48 us                                                | 6.29 us: 1.03x faster                                                  |
| mako                    | 9.83 ms                                                | 9.56 ms: 1.03x faster                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| spectral_norm           | 98.1 ms                                                | 95.6 ms: 1.03x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.18 ms: 1.03x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.61 ms: 1.02x faster                                                  |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| nqueens                 | 83.8 ms                                                | 82.0 ms: 1.02x faster                                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                   |
| xml_etree_process       | 53.7 ms                                                | 52.8 ms: 1.02x faster                                                  |
| thrift                  | 760 us                                                 | 748 us: 1.02x faster                                                   |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                  |
| python_startup          | 8.58 ms                                                | 8.48 ms: 1.01x faster                                                  |
| chameleon               | 6.38 ms                                                | 6.31 ms: 1.01x faster                                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.99 us: 1.01x faster                                                  |
| django_template         | 32.3 ms                                                | 32.1 ms: 1.01x faster                                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.3 ms: 1.01x slower                                                  |
| pickle_dict             | 31.2 us                                                | 31.3 us: 1.01x slower                                                  |
| async_generators        | 356 ms                                                 | 358 ms: 1.01x slower                                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.12 ms: 1.01x slower                                                  |
| unpack_sequence         | 44.5 ns                                                | 45.1 ns: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| unpickle                | 13.3 us                                                | 13.6 us: 1.02x slower                                                  |
| coverage                | 99.3 ms                                                | 102 ms: 1.02x slower                                                   |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                 |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                   |
| regex_effbot            | 3.46 ms                                                | 3.55 ms: 1.03x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.13 us: 1.03x slower                                                  |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                   |
| nbody                   | 90.0 ms                                                | 93.7 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (5): crypto_pyaes, async_tree_memoization, bench_mp_pool, telco, async_tree_none
Ignored benchmarks (10) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy
