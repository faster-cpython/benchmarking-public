
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: darwin-arm64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 168 ms: 1.20x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.53 ms: 1.28x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| html5lib       | 44.2 ms                                                | 36.4 ms: 1.21x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.3 ms: 1.43x faster                                                 |
| float          | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.2 ms: 1.25x faster                                                 |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.12 ms: 1.37x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 214 us: 1.32x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 161 us: 1.26x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 36.3 ms: 1.23x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.7 ms: 1.10x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 50.4 ms: 1.07x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.57 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 69.6 ms: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| unpickle             | 9.89 us                                                | 9.63 us: 1.03x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.60 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.24 ms: 1.45x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 30.4 ms: 1.22x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 64.2 ns: 1.86x faster                                                 |
| deltablue               | 5.14 ms                                                | 2.85 ms: 1.80x faster                                                 |
| richards                | 51.4 ms                                                | 32.1 ms: 1.60x faster                                                 |
| scimark_lu              | 109 ms                                                 | 70.9 ms: 1.54x faster                                                 |
| raytrace                | 325 ms                                                 | 222 ms: 1.47x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 335 ms: 1.46x faster                                                  |
| mako                    | 10.5 ms                                                | 7.24 ms: 1.45x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 54.2 ms: 1.44x faster                                                 |
| nbody                   | 93.3 ms                                                | 65.3 ms: 1.43x faster                                                 |
| go                      | 165 ms                                                 | 118 ms: 1.40x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.12 ms: 1.37x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.00 ms: 1.36x faster                                                 |
| async_tree_none         | 400 ms                                                 | 297 ms: 1.35x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 756 ms: 1.35x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.19 ms: 1.33x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 214 us: 1.32x faster                                                  |
| pycparser               | 916 ms                                                 | 704 ms: 1.30x faster                                                  |
| thrift                  | 580 us                                                 | 447 us: 1.30x faster                                                  |
| chaos                   | 66.7 ms                                                | 51.5 ms: 1.29x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 56.2 ms: 1.29x faster                                                 |
| pyflate                 | 453 ms                                                 | 352 ms: 1.29x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 74.4 ms: 1.29x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.53 ms: 1.28x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 694 us: 1.27x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 161 us: 1.26x faster                                                  |
| hexiom                  | 6.32 ms                                                | 5.01 ms: 1.26x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.68 us: 1.26x faster                                                 |
| logging_format          | 4.97 us                                                | 3.96 us: 1.25x faster                                                 |
| float                   | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                 |
| regex_compile           | 96.4 ms                                                | 77.2 ms: 1.25x faster                                                 |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.78 ms: 1.24x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 36.3 ms: 1.23x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 30.4 ms: 1.22x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.5 ms: 1.22x faster                                                 |
| scimark_sor             | 126 ms                                                 | 104 ms: 1.22x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.4 ms: 1.21x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 502 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 556 ms: 1.20x faster                                                  |
| 2to3                    | 201 ms                                                 | 168 ms: 1.20x faster                                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| pprint_pformat          | 1.23 sec                                               | 1.03 sec: 1.20x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 32.1 ms: 1.18x faster                                                 |
| scimark_fft             | 230 ms                                                 | 198 ms: 1.16x faster                                                  |
| fannkuch                | 317 ms                                                 | 273 ms: 1.16x faster                                                  |
| mypy2                   | 307 ms                                                 | 264 ms: 1.16x faster                                                  |
| dask                    | 265 ms                                                 | 230 ms: 1.15x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 473 us: 1.15x faster                                                  |
| async_generators        | 234 ms                                                 | 207 ms: 1.13x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 176 ms: 1.11x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 31.0 us: 1.11x faster                                                 |
| deepcopy                | 281 us                                                 | 253 us: 1.11x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 12.0 ms: 1.11x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.7 ms: 1.10x faster                                                 |
| sympy_expand            | 275 ms                                                 | 251 ms: 1.10x faster                                                  |
| nqueens                 | 68.2 ms                                                | 62.2 ms: 1.10x faster                                                 |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.17 us: 1.09x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                  |
| sympy_str               | 169 ms                                                 | 157 ms: 1.08x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 50.4 ms: 1.07x faster                                                 |
| telco                   | 3.63 ms                                                | 3.41 ms: 1.07x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 87.9 ms: 1.07x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.05x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.57 us: 1.04x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 69.6 ms: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| unpickle                | 9.89 us                                                | 9.63 us: 1.03x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 653 ms: 1.02x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.9 ms: 1.02x faster                                                 |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.66 sec: 1.00x faster                                                |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| meteor_contest          | 78.1 ms                                                | 78.6 ms: 1.01x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| comprehensions          | 17.6 us                                                | 17.8 us: 1.01x slower                                                 |
| generators              | 32.7 ms                                                | 33.6 ms: 1.03x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                 |
| pickle                  | 7.35 us                                                | 7.60 us: 1.03x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 44.6 ms: 1.12x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.15x slower                                                 |
| unpack_sequence         | 37.4 ns                                                | 52.7 ns: 1.41x slower                                                 |
| coverage                | 42.0 ms                                                | 60.7 ms: 1.44x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                          |
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
