
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: darwin-arm64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.01x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                   |
| chameleon      | 4.57 ms                                                | 4.50 ms: 1.02x faster                                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| html5lib       | 34.7 ms                                                | 36.1 ms: 1.04x slower                                                  |
| tornado_http   | 72.4 ms                                                | 68.2 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.4 ms: 1.02x faster                                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| float          | 53.0 ms                                                | 57.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_compile  | 76.7 ms                                                | 75.7 ms: 1.01x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.07 ms: 1.27x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 92.9 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 66.3 ms: 1.04x faster                                                  |
| xml_etree_generate   | 48.8 ms                                                | 48.4 ms: 1.01x faster                                                  |
| xml_etree_process    | 35.2 ms                                                | 35.1 ms: 1.00x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| unpickle             | 9.70 us                                                | 9.79 us: 1.01x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 161 us: 1.01x slower                                                   |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 209 us: 1.05x slower                                                   |
| pickle               | 7.17 us                                                | 7.61 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.54 ms: 1.24x faster                                                  |
| python_startup         | 11.5 ms                                                | 9.49 ms: 1.21x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.29 ms: 1.16x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.6 ms: 1.05x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 29.5 ms: 1.01x faster                                                  |
| django_template | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.4 ms: 1.36x faster                                                  |
| json_dumps              | 7.72 ms                                                | 6.07 ms: 1.27x faster                                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.54 ms: 1.24x faster                                                  |
| python_startup          | 11.5 ms                                                | 9.49 ms: 1.21x faster                                                  |
| mako                    | 8.49 ms                                                | 7.29 ms: 1.16x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 92.9 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.80 ms: 1.14x faster                                                  |
| tornado_http            | 72.4 ms                                                | 68.2 ms: 1.06x faster                                                  |
| logging_silent          | 68.0 ns                                                | 64.2 ns: 1.06x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.6 ms: 1.05x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 66.3 ms: 1.04x faster                                                  |
| async_tree_memoization  | 336 ms                                                 | 322 ms: 1.04x faster                                                   |
| bench_thread_pool       | 473 us                                                 | 454 us: 1.04x faster                                                   |
| richards                | 32.2 ms                                                | 31.0 ms: 1.04x faster                                                  |
| dulwich_log             | 29.9 ms                                                | 29.2 ms: 1.02x faster                                                  |
| bench_mp_pool           | 43.2 ms                                                | 42.2 ms: 1.02x faster                                                  |
| coverage                | 58.6 ms                                                | 57.4 ms: 1.02x faster                                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| nbody                   | 65.5 ms                                                | 64.4 ms: 1.02x faster                                                  |
| chameleon               | 4.57 ms                                                | 4.50 ms: 1.02x faster                                                  |
| regex_compile           | 76.7 ms                                                | 75.7 ms: 1.01x faster                                                  |
| scimark_lu              | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| scimark_fft             | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| genshi_xml              | 29.8 ms                                                | 29.5 ms: 1.01x faster                                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.79 ms: 1.01x faster                                                  |
| xml_etree_generate      | 48.8 ms                                                | 48.4 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| xml_etree_process       | 35.2 ms                                                | 35.1 ms: 1.00x faster                                                  |
| spectral_norm           | 72.8 ms                                                | 72.9 ms: 1.00x slower                                                  |
| telco                   | 3.39 ms                                                | 3.42 ms: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| unpickle                | 9.70 us                                                | 9.79 us: 1.01x slower                                                  |
| thrift                  | 433 us                                                 | 438 us: 1.01x slower                                                   |
| sympy_sum               | 86.0 ms                                                | 87.1 ms: 1.01x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 161 us: 1.01x slower                                                   |
| sqlglot_optimize        | 31.2 ms                                                | 31.6 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 543 ms: 1.02x slower                                                   |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                   |
| django_template         | 21.0 ms                                                | 21.4 ms: 1.02x slower                                                  |
| sympy_expand            | 243 ms                                                 | 248 ms: 1.02x slower                                                   |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                                  |
| sympy_str               | 152 ms                                                 | 154 ms: 1.02x slower                                                   |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                                  |
| chaos                   | 49.5 ms                                                | 50.5 ms: 1.02x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.3 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.16 ms: 1.03x slower                                                  |
| json                    | 2.77 ms                                                | 2.88 ms: 1.04x slower                                                  |
| fannkuch                | 261 ms                                                 | 270 ms: 1.04x slower                                                   |
| async_tree_io           | 706 ms                                                 | 733 ms: 1.04x slower                                                   |
| logging_simple          | 3.50 us                                                | 3.64 us: 1.04x slower                                                  |
| sqlglot_parse           | 957 us                                                 | 995 us: 1.04x slower                                                   |
| hexiom                  | 4.73 ms                                                | 4.92 ms: 1.04x slower                                                  |
| html5lib                | 34.7 ms                                                | 36.1 ms: 1.04x slower                                                  |
| logging_format          | 3.78 us                                                | 3.93 us: 1.04x slower                                                  |
| async_generators        | 195 ms                                                 | 204 ms: 1.05x slower                                                   |
| meteor_contest          | 73.8 ms                                                | 77.6 ms: 1.05x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 209 us: 1.05x slower                                                   |
| raytrace                | 207 ms                                                 | 219 ms: 1.06x slower                                                   |
| pickle                  | 7.17 us                                                | 7.61 us: 1.06x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 1.01 sec: 1.06x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 496 ms: 1.07x slower                                                   |
| float                   | 53.0 ms                                                | 57.0 ms: 1.08x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.07 us: 1.08x slower                                                  |
| deepcopy                | 224 us                                                 | 243 us: 1.09x slower                                                   |
| go                      | 109 ms                                                 | 118 ms: 1.09x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.41 us: 1.11x slower                                                  |
| coroutines              | 17.7 ms                                                | 19.9 ms: 1.12x slower                                                  |
| pyflate                 | 311 ms                                                 | 351 ms: 1.13x slower                                                   |
| deepcopy_memo           | 26.3 us                                                | 30.1 us: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                   |
| generators              | 28.8 ms                                                | 33.8 ms: 1.17x slower                                                  |
| scimark_sor             | 83.0 ms                                                | 98.4 ms: 1.18x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 55.5 ms: 1.20x slower                                                  |
| unpack_sequence         | 33.6 ns                                                | 61.5 ns: 1.83x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (5): unpickle_list, nqueens, mdp, async_tree_none, pycparser
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy
