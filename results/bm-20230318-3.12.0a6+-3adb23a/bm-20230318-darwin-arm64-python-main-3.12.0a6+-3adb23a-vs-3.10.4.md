
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                   |
| chameleon      | 5.79 ms                                                | 4.48 ms: 1.29x faster                                  |
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| html5lib       | 44.2 ms                                                | 35.7 ms: 1.24x faster                                  |
| tornado_http   | 91.5 ms                                                | 69.5 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 60.7 ms: 1.54x faster                                  |
| float          | 72.4 ms                                                | 52.7 ms: 1.37x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.9 ms: 1.27x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.07x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.68 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.48x faster                                   |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.28 ms: 1.34x faster                                  |
| xml_etree_process    | 44.8 ms                                                | 36.7 ms: 1.22x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 97.4 ms: 1.09x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 51.8 ms: 1.04x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.3 ms: 1.03x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.64 us: 1.02x faster                                  |
| unpickle             | 9.89 us                                                | 9.77 us: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.41 us: 1.01x slower                                  |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 11.0 ms: 1.09x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 8.99 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.44 ms: 1.41x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.3 ms: 1.27x faster                                  |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.24x faster                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.56 ms: 2.01x faster                                  |
| logging_silent          | 119 ns                                                 | 66.9 ns: 1.78x faster                                  |
| richards                | 51.4 ms                                                | 30.7 ms: 1.68x faster                                  |
| nbody                   | 93.3 ms                                                | 60.7 ms: 1.54x faster                                  |
| scimark_lu              | 109 ms                                                 | 71.2 ms: 1.53x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 449 ms: 1.49x faster                                   |
| go                      | 165 ms                                                 | 111 ms: 1.49x faster                                   |
| scimark_sor             | 126 ms                                                 | 85.2 ms: 1.48x faster                                  |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.48x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 333 ms: 1.47x faster                                   |
| raytrace                | 325 ms                                                 | 222 ms: 1.47x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.40 ms: 1.43x faster                                  |
| crypto_pyaes            | 78.1 ms                                                | 54.6 ms: 1.43x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 50.7 ms: 1.43x faster                                  |
| mako                    | 10.5 ms                                                | 7.44 ms: 1.41x faster                                  |
| chaos                   | 66.7 ms                                                | 47.4 ms: 1.41x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 145 us: 1.40x faster                                   |
| async_tree_none         | 400 ms                                                 | 288 ms: 1.39x faster                                   |
| float                   | 72.4 ms                                                | 52.7 ms: 1.37x faster                                  |
| async_tree_io           | 1.02 sec                                               | 743 ms: 1.37x faster                                   |
| pyflate                 | 453 ms                                                 | 332 ms: 1.37x faster                                   |
| pycparser               | 916 ms                                                 | 676 ms: 1.35x faster                                   |
| json_dumps              | 8.40 ms                                                | 6.28 ms: 1.34x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 25.8 us: 1.33x faster                                  |
| spectral_norm           | 95.8 ms                                                | 72.1 ms: 1.33x faster                                  |
| tornado_http            | 91.5 ms                                                | 69.5 ms: 1.32x faster                                  |
| chameleon               | 5.79 ms                                                | 4.48 ms: 1.29x faster                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.06 ms: 1.29x faster                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.23 ms: 1.28x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 967 ms: 1.27x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 475 ms: 1.27x faster                                   |
| thrift                  | 580 us                                                 | 456 us: 1.27x faster                                   |
| regex_compile           | 96.4 ms                                                | 75.9 ms: 1.27x faster                                  |
| genshi_xml              | 37.2 ms                                                | 29.3 ms: 1.27x faster                                  |
| logging_simple          | 4.63 us                                                | 3.66 us: 1.26x faster                                  |
| deepcopy                | 281 us                                                 | 222 us: 1.26x faster                                   |
| logging_format          | 4.97 us                                                | 3.95 us: 1.26x faster                                  |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                  |
| create_gc_cycles        | 880 us                                                 | 705 us: 1.25x faster                                   |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                  |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.24x faster                                  |
| html5lib                | 44.2 ms                                                | 35.7 ms: 1.24x faster                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.19 ms: 1.24x faster                                  |
| scimark_fft             | 230 ms                                                 | 187 ms: 1.23x faster                                   |
| xml_etree_process       | 44.8 ms                                                | 36.7 ms: 1.22x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 548 ms: 1.22x faster                                   |
| 2to3                    | 201 ms                                                 | 165 ms: 1.22x faster                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.96 us: 1.21x faster                                  |
| fannkuch                | 317 ms                                                 | 262 ms: 1.21x faster                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.86 ms: 1.21x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 32.0 ms: 1.19x faster                                  |
| docutils                | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| generators              | 32.7 ms                                                | 27.8 ms: 1.18x faster                                  |
| mypy2                   | 307 ms                                                 | 264 ms: 1.16x faster                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 64.5 ms: 1.16x faster                                  |
| bench_thread_pool       | 546 us                                                 | 472 us: 1.16x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.13x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.13x faster                                   |
| unpack_sequence         | 37.4 ns                                                | 33.3 ns: 1.12x faster                                  |
| mdp                     | 1.66 sec                                               | 1.49 sec: 1.11x faster                                 |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.11x faster                                  |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                   |
| json                    | 3.08 ms                                                | 2.80 ms: 1.10x faster                                  |
| nqueens                 | 68.2 ms                                                | 62.1 ms: 1.10x faster                                  |
| sympy_str               | 169 ms                                                 | 154 ms: 1.10x faster                                   |
| xml_etree_parse         | 106 ms                                                 | 97.4 ms: 1.09x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                  |
| python_startup          | 11.9 ms                                                | 11.0 ms: 1.09x faster                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.07x faster                                   |
| sympy_sum               | 93.6 ms                                                | 88.3 ms: 1.06x faster                                  |
| meteor_contest          | 78.1 ms                                                | 73.8 ms: 1.06x faster                                  |
| xml_etree_generate      | 54.2 ms                                                | 51.8 ms: 1.04x faster                                  |
| telco                   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.3 ms: 1.03x faster                                  |
| unpickle_list           | 2.69 us                                                | 2.64 us: 1.02x faster                                  |
| unpickle                | 9.89 us                                                | 9.77 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.41 us: 1.01x slower                                  |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                  |
| python_startup_no_site  | 8.88 ms                                                | 8.99 ms: 1.01x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                  |
| comprehensions          | 17.6 us                                                | 17.9 us: 1.02x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.68 ms: 1.09x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 44.8 ms: 1.13x slower                                  |
| async_generators        | 234 ms                                                 | 266 ms: 1.14x slower                                   |
| dask                    | 265 ms                                                 | 322 ms: 1.21x slower                                   |
| coverage                | 42.0 ms                                                | 56.0 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                           |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
